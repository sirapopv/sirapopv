@echo off
REM YouTube to Podcast Converter - Windows Setup
REM Run this ONCE to set up everything

echo ========================================
echo   YouTube to Podcast Converter
echo   First-Time Setup
echo ========================================
echo.
echo This will install everything you need.
echo This may take a few minutes...
echo.
pause

REM Check Python
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python 3.8 or newer from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

REM Check ffmpeg
echo Checking ffmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: ffmpeg is not installed.
    echo.
    echo You need ffmpeg for video creation.
    echo.
    echo Download from: https://www.gyan.dev/ffmpeg/builds/
    echo Get "ffmpeg-release-essentials.zip"
    echo Extract and add to PATH
    echo.
    echo Or install via Chocolatey: choco install ffmpeg
    echo.
    set /p continue="Continue anyway? (y/n): "
    if /i not "%continue%"=="y" exit /b 1
) else (
    echo ffmpeg found!
)
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist "venv" (
    echo Virtual environment already exists.
) else (
    python -m venv venv
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to create virtual environment.
        echo.
        pause
        exit /b 1
    )
    echo Virtual environment created!
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo.
echo Installing dependencies...
echo This may take a few minutes...
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies.
    echo.
    pause
    exit /b 1
)

REM Create directories
echo.
echo Creating directories...
if not exist "output" mkdir output
if not exist "settings" mkdir settings

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env >nul 2>&1
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Get your Google Gemini API key from:
echo    https://makersuite.google.com/app/apikey
echo.
echo 2. Double-click START.bat to launch the app
echo.
echo 3. Enter your API key in the app (only needed once)
echo.
echo ========================================
echo.
echo You can now close this window.
echo.
pause
