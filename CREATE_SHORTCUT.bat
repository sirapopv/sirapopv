@echo off
REM Creates a desktop shortcut for YouTube to Podcast Converter

echo ========================================
echo   Creating Desktop Shortcut
echo ========================================
echo.

REM Get current directory
set CURRENT_DIR=%~dp0

REM Create VBScript to create shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\YouTube Podcast Converter.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%CURRENT_DIR%START.bat" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%CURRENT_DIR%" >> CreateShortcut.vbs
echo oLink.Description = "YouTube to Podcast Converter" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

REM Execute the script
cscript CreateShortcut.vbs >nul

REM Clean up
del CreateShortcut.vbs

echo.
echo ========================================
echo   Shortcut Created!
echo ========================================
echo.
echo A shortcut has been created on your desktop.
echo You can now double-click it to start the app!
echo.
pause
