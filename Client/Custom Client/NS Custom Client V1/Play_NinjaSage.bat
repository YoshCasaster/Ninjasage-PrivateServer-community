@echo off
setlocal enabledelayedexpansion
title Ninja Sage Launcher

:: Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Ninja Sage requires Administrator privileges to connect to the server.
    echo Please right-click this file and select "Run as administrator".
    pause
    exit /b
)

set HOSTS_FILE=%WINDIR%\System32\drivers\etc\hosts
set SERVER_IP=202.10.48.153

echo [Ninja Sage] Checking server connection settings...

:: Check and add Clan domain
findstr /C:"%SERVER_IP% clan.ninjasage.id" "%HOSTS_FILE%" >nul
if %errorLevel% neq 0 (
    echo %SERVER_IP% clan.ninjasage.id >> "%HOSTS_FILE%"
)

:: Check and add Crew domain
findstr /C:"%SERVER_IP% crew.ninjasage.id" "%HOSTS_FILE%" >nul
if %errorLevel% neq 0 (
    echo %SERVER_IP% crew.ninjasage.id >> "%HOSTS_FILE%"
)

echo [Ninja Sage] Connection optimized! Starting game...
start "" "NSCUSTOM.exe"

exit
