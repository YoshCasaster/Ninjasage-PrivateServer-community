using System;
using System.Diagnostics;
using System.IO;
using System.Security.Principal;
using System.Windows.Forms;

namespace NinjaSageLauncher
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            try
            {
                if (!IsAdministrator())
                {
                    // Restart program and run as admin
                    var exeName = Process.GetCurrentProcess().MainModule.FileName;
                    ProcessStartInfo startInfo = new ProcessStartInfo(exeName);
                    startInfo.Verb = "runas";
                    startInfo.UseShellExecute = true;
                    Process.Start(startInfo);
                    return;
                }

                // We are admin, update hosts file
                string hostsPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System), @"drivers\etc\hosts");
                string ip = "202.10.48.153";
                string clanUrl = "clan.ninjasage.id";
                string crewUrl = "crew.ninjasage.id";
                
                string hostsContent = File.Exists(hostsPath) ? File.ReadAllText(hostsPath) : "";
                
                bool changed = false;
                if (!hostsContent.Contains(clanUrl))
                {
                    hostsContent += "\r\n" + ip + " " + clanUrl;
                    changed = true;
                }
                if (!hostsContent.Contains(crewUrl))
                {
                    hostsContent += "\r\n" + ip + " " + crewUrl;
                    changed = true;
                }

                if (changed)
                {
                    // Remove read-only attribute if exists
                    FileAttributes attrs = File.GetAttributes(hostsPath);
                    if ((attrs & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
                    {
                        File.SetAttributes(hostsPath, attrs & ~FileAttributes.ReadOnly);
                    }
                    File.WriteAllText(hostsPath, hostsContent);
                }

                // Launch the actual game
                string gameExe = "NSCUSTOM.exe";
                if (File.Exists(gameExe))
                {
                    Process.Start(gameExe);
                }
                else
                {
                    MessageBox.Show("Could not find NSCUSTOM.exe! Make sure this Launcher is in the same folder as the game.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Failed to launch the game: " + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private static bool IsAdministrator()
        {
            WindowsIdentity identity = WindowsIdentity.GetCurrent();
            WindowsPrincipal principal = new WindowsPrincipal(identity);
            return principal.IsInRole(WindowsBuiltInRole.Administrator);
        }
    }
}
