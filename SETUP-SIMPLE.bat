@echo off
REM Simple Setup Script - Window will NOT close automatically
REM Use this if other setup scripts close too quickly

title YouTube Converter Setup

:start
cls
echo ========================================
echo   YouTube to Podcast Converter
echo   Simple Setup (Window stays open)
echo ========================================
echo.
echo This window will stay open so you can
echo see any error messages.
echo.
echo Press any key to start setup...
pause >nul

cls
echo ========================================
echo   Step 1: Checking Python
echo ========================================
echo.

python --version
if errorlevel 1 (
    echo.
    echo [ERROR] Python is not installed!
    echo.
    echo What to do:
    echo 1. Go to: https://www.python.org/downloads/
    echo 2. Download Python (3.8 or newer)
    echo 3. Run installer
    echo 4. IMPORTANT: Check "Add Python to PATH"
    echo 5. After installation, CLOSE this window
    echo 6. OPEN A NEW command prompt
    echo 7. Run this script again
    echo.
    goto :error
)

echo.
echo Python found! Continuing...
timeout /t 2 /nobreak >nul

cls
echo ========================================
echo   Step 2: Creating Virtual Environment
echo ========================================
echo.

if exist "venv" (
    echo Virtual environment already exists.
    echo Using existing virtual environment...
    echo.
) else (
    echo Creating virtual environment...
    echo Please wait...
    echo.
    python -m venv venv

    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to create virtual environment!
        echo.
        echo Solutions:
        echo 1. Run this script as Administrator
        echo 2. Move the folder to C:\youtube-converter
        echo 3. Check antivirus isn't blocking Python
        echo.
        goto :error
    )

    echo Virtual environment created successfully!
    echo.
)

timeout /t 2 /nobreak >nul

cls
echo ========================================
echo   Step 3: Activating Virtual Environment
echo ========================================
echo.

call venv\Scripts\activate.bat
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to activate virtual environment!
    echo.
    goto :error
)

echo Virtual environment activated!
timeout /t 2 /nobreak >nul

cls
echo ========================================
echo   Step 4: Upgrading pip
echo ========================================
echo.

python -m pip install --upgrade pip
echo.
echo pip upgraded!
timeout /t 2 /nobreak >nul

cls
echo ========================================
echo   Step 5: Installing Dependencies
echo   (This takes 5-10 minutes)
echo ========================================
echo.
echo Installing packages...
echo You'll see progress below:
echo.

python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ========================================
    echo   [ERROR] Installation Failed!
    echo ========================================
    echo.
    echo What probably happened:
    echo - Internet connection problem
    echo - Firewall/Antivirus blocking
    echo - PyPI server timeout
    echo.
    echo SOLUTIONS TO TRY:
    echo.
    echo Solution 1 - Try with longer timeout:
    echo   venv\Scripts\activate
    echo   pip install --timeout=300 -r requirements.txt
    echo.
    echo Solution 2 - Try alternative setup:
    echo   Double-click SETUP-ALTERNATIVE.bat
    echo.
    echo Solution 3 - Install one by one manually:
    echo   See TROUBLESHOOTING.md
    echo.
    goto :error
)

cls
echo ========================================
echo   Step 6: Creating Directories
echo ========================================
echo.

if not exist "output" mkdir output
if not exist "settings" mkdir settings

echo Directories created!
timeout /t 2 /nobreak >nul

cls
echo ========================================
echo   SUCCESS! Setup Complete!
echo ========================================
echo.
echo Everything installed successfully!
echo.
echo NEXT STEPS:
echo.
echo 1. Get API Key from:
echo    https://makersuite.google.com/app/apikey
echo.
echo 2. Double-click START.bat to launch the app
echo.
echo 3. Enter your API key in the sidebar
echo.
echo 4. Start converting videos!
echo.
echo ========================================
echo.
echo Press any key to close...
pause >nul
exit /b 0

:error
echo.
echo ========================================
echo.
echo The window will stay open so you can
echo read the error message above.
echo.
echo For more help, check TROUBLESHOOTING.md
echo.
echo ========================================
echo.
echo Press any key to close...
pause >nul
exit /b 1
