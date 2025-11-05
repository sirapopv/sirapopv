@echo off
REM Quick Fix for Installation Issues
REM Installs packages without strict version requirements

title Quick Fix Installation

echo ========================================
echo   QUICK FIX - Installation
echo   (Without version constraints)
echo ========================================
echo.
echo This installs packages without requiring
echo specific versions, which often fixes
echo compilation errors like Pillow.
echo.
pause

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Run as Administrator or check Python installation
        pause
        exit /b 1
    )
)

REM Activate venv
call venv\Scripts\activate.bat

echo.
echo Upgrading pip, wheel, and setuptools...
python -m pip install --upgrade pip wheel setuptools
echo.

echo ========================================
echo Installing packages (no version locks)
echo ========================================
echo.

echo [1/10] youtube-transcript-api...
pip install youtube-transcript-api

echo [2/10] yt-dlp...
pip install yt-dlp

echo [3/10] google-generativeai...
pip install google-generativeai

echo [4/10] gtts...
pip install gtts

echo.
echo [5/10] Pillow (this is the problematic one)...
echo Trying to install with pre-built wheel...
pip install --upgrade Pillow
if errorlevel 1 (
    echo.
    echo Pillow failed with standard method.
    echo Trying without cache...
    pip install --no-cache-dir Pillow
    if errorlevel 1 (
        echo.
        echo ========================================
        echo   Pillow Installation Failed
        echo ========================================
        echo.
        echo This is common on Windows.
        echo.
        echo QUICK FIX:
        echo 1. Install Visual C++ Build Tools:
        echo    https://aka.ms/vs/17/release/vs_BuildTools.exe
        echo.
        echo 2. Or download pre-built Pillow:
        echo    https://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
        echo.
        echo 3. Or continue WITHOUT Pillow:
        echo    (App will work but can't generate thumbnails)
        echo.
        set /p skip="Continue without Pillow? (y/n): "
        if /i "%skip%"=="n" (
            echo.
            echo Please install Pillow manually and run this script again.
            pause
            exit /b 1
        )
        echo.
        echo Continuing without Pillow...
    )
)

echo [6/10] pyyaml...
pip install pyyaml

echo [7/10] python-dotenv...
pip install python-dotenv

echo [8/10] click...
pip install click

echo [9/10] rich...
pip install rich

echo.
echo [10/10] streamlit (large package, may take 2-3 min)...
pip install streamlit

if errorlevel 1 (
    echo.
    echo Streamlit installation failed.
    echo Trying without cache...
    pip install --no-cache-dir streamlit
)

echo.
echo ========================================
echo Creating directories...
echo ========================================
if not exist "output" mkdir output
if not exist "settings" mkdir settings

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo Installed packages:
pip list | findstr -i "youtube transcript yt-dlp google-generativeai gtts pillow pyyaml python-dotenv click rich streamlit"
echo.
echo ========================================
echo.
echo Next: Double-click START.bat to launch!
echo.
pause
