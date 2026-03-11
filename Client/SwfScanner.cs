using System;
using System.IO;
using System.IO.Compression;
using System.Text;
using System.Text.RegularExpressions;

namespace SwfScanner
{
    class Program
    {
        static void Main(string[] args)
        {
            string swfPath = @"c:\laragon\www\ninjasage\Client\Custom Client\NS Custom Client V1\NinjaSage.swf";
            string outPath = @"c:\laragon\www\ninjasage\Client\swf_strings.txt";
            byte[] fileBytes = File.ReadAllBytes(swfPath);
            byte[] uncompressedData = fileBytes;

            // CWS = Compressed SWF (Zlib)
            if (fileBytes[0] == 'C' && fileBytes[1] == 'W' && fileBytes[2] == 'S')
            {
                using (MemoryStream ms = new MemoryStream(fileBytes, 8, fileBytes.Length - 8))
                {
                    ms.Seek(2, SeekOrigin.Begin);
                    using (DeflateStream deflate = new DeflateStream(ms, CompressionMode.Decompress))
                    {
                        using (MemoryStream output = new MemoryStream())
                        {
                            deflate.CopyTo(output);
                            uncompressedData = output.ToArray();
                        }
                    }
                }
            }

            // Extract all readable strings (ASCII, length >= 6)
            string content = Encoding.ASCII.GetString(uncompressedData);
            MatchCollection matches = Regex.Matches(content, @"[a-zA-Z0-9.:/_\-]{6,}");
            using (StreamWriter writer = new StreamWriter(outPath))
            {
                foreach(Match m in matches)
                {
                    writer.WriteLine(m.Value);
                }
            }
        }
    }
}
