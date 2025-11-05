@echo off
REM YouTube to Podcast Converter - Windows Setup (Improved)
REM Run this ONCE to set up everything

echo ========================================
echo   YouTube to Podcast Converter
echo   First-Time Setup (v2.0)
echo ========================================
echo.
echo This will install everything you need.
echo.
pause

REM Check if running in correct directory
if not exist "requirements.txt" (
    echo.
    echo ERROR: requirements.txt not found!
    echo Please run this script from the project directory.
    echo.
    pause
    exit /b 1
)

REM Check Python
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.8 or newer from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    echo.
    echo After installing Python:
    echo 1. Close this window
    echo 2. Open a NEW command prompt
    echo 3. Run SETUP.bat again
    echo.
    pause
    exit /b 1
)

python --version
echo Python OK!
echo.

REM Check Python version
echo [2/6] Checking Python version...
python -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python version is too old!
    echo Please install Python 3.8 or newer.
    python --version
    echo.
    pause
    exit /b 1
)
echo Python version OK!
echo.

REM Check pip
echo [3/6] Checking pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: pip is not installed!
    echo Installing pip...
    python -m ensurepip --default-pip
    if errorlevel 1 (
        echo Failed to install pip!
        pause
        exit /b 1
    )
)
python -m pip --version
echo pip OK!
echo.

REM Check ffmpeg (warning only)
echo [4/6] Checking ffmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: ffmpeg is not installed.
    echo You need ffmpeg for video creation.
    echo.
    echo Quick install options:
    echo.
    echo Option 1 - Using Chocolatey (if installed):
    echo   choco install ffmpeg
    echo.
    echo Option 2 - Manual download:
    echo   1. Go to: https://www.gyan.dev/ffmpeg/builds/
    echo   2. Download "ffmpeg-release-essentials.zip"
    echo   3. Extract to C:\ffmpeg
    echo   4. Add C:\ffmpeg\bin to PATH
    echo.
    echo Option 3 - Using winget (Windows 10/11):
    echo   winget install ffmpeg
    echo.
    set /p continue="Continue without ffmpeg? (y/n): "
    if /i not "%continue%"=="y" (
        echo.
        echo Please install ffmpeg and run SETUP.bat again.
        pause
        exit /b 1
    )
    echo.
    echo Continuing without ffmpeg...
    echo (You can install it later)
    echo.
) else (
    ffmpeg -version | findstr "version"
    echo ffmpeg OK!
    echo.
)

REM Create virtual environment
echo [5/6] Setting up virtual environment...
if exist "venv" (
    echo Virtual environment already exists.
    echo.
) else (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to create virtual environment.
        echo.
        echo Troubleshooting:
        echo 1. Make sure you have write permissions in this folder
        echo 2. Try running as Administrator (right-click SETUP.bat ^> Run as Administrator)
        echo 3. Check if antivirus is blocking Python
        echo.
        pause
        exit /b 1
    )
    echo Virtual environment created!
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo.
    echo ERROR: Failed to activate virtual environment.
    echo.
    pause
    exit /b 1
)
echo Virtual environment activated!
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo pip upgraded!
echo.

REM Install requirements
echo [6/6] Installing dependencies...
echo This may take 5-10 minutes depending on your internet speed...
echo.
echo Installing packages (this will show progress):
echo.

python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ========================================
    echo   ERROR: Failed to install dependencies
    echo ========================================
    echo.
    echo Common solutions:
    echo.
    echo 1. Check your internet connection
    echo.
    echo 2. Try installing with increased timeout:
    echo    venv\Scripts\activate
    echo    pip install --timeout=120 -r requirements.txt
    echo.
    echo 3. Try installing packages one by one:
    echo    See TROUBLESHOOTING.md for details
    echo.
    echo 4. Disable antivirus temporarily
    echo.
    echo 5. Run as Administrator:
    echo    Right-click SETUP.bat ^> Run as Administrator
    echo.
    echo 6. Clear pip cache and retry:
    echo    pip cache purge
    echo    pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo All dependencies installed successfully!
echo.

REM Create directories
echo Creating directories...
if not exist "output" mkdir output
if not exist "settings" mkdir settings
echo Directories created!
echo.

REM Create .env file
if not exist ".env" (
    if exist ".env.example" (
        echo Creating .env file...
        copy .env.example .env >nul 2>&1
        echo .env file created!
    )
)
echo.

echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Next steps:
echo.
echo 1. Get your Google Gemini API key:
echo    https://makersuite.google.com/app/apikey
echo.
echo 2. Double-click START.bat to launch the app
echo.
echo 3. Enter your API key in the sidebar (one-time)
echo.
echo 4. Start converting videos!
echo.
echo ========================================
echo.
echo Tip: Run CREATE_SHORTCUT.bat to add a desktop icon!
echo.
pause
