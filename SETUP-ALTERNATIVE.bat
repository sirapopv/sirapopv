@echo off
REM Alternative Setup Script - Installs packages one by one
REM Use this if SETUP.bat fails

echo ========================================
echo   Alternative Setup Method
echo   (Slower but more reliable)
echo ========================================
echo.
echo This script installs packages ONE BY ONE
echo so you can see exactly where any error occurs.
echo.
pause

REM Check Python
echo Checking Python...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo.

REM Create venv
echo Creating virtual environment...
if exist "venv" (
    echo Virtual environment exists, using it...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)
echo.

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install packages one by one
echo ========================================
echo Installing packages (1 of 10): youtube-transcript-api
echo ========================================
pip install youtube-transcript-api==0.6.2
if errorlevel 1 (
    echo FAILED: youtube-transcript-api
    pause
)
echo.

echo ========================================
echo Installing packages (2 of 10): yt-dlp
echo ========================================
pip install yt-dlp==2024.8.6
if errorlevel 1 (
    echo FAILED: yt-dlp
    pause
)
echo.

echo ========================================
echo Installing packages (3 of 10): google-generativeai
echo ========================================
pip install google-generativeai==0.8.3
if errorlevel 1 (
    echo FAILED: google-generativeai
    pause
)
echo.

echo ========================================
echo Installing packages (4 of 10): gtts
echo ========================================
pip install gtts==2.5.4
if errorlevel 1 (
    echo FAILED: gtts
    pause
)
echo.

echo ========================================
echo Installing packages (5 of 10): Pillow
echo ========================================
pip install Pillow==10.4.0
if errorlevel 1 (
    echo FAILED: Pillow
    pause
)
echo.

echo ========================================
echo Installing packages (6 of 10): pyyaml
echo ========================================
pip install pyyaml==6.0.2
if errorlevel 1 (
    echo FAILED: pyyaml
    pause
)
echo.

echo ========================================
echo Installing packages (7 of 10): python-dotenv
echo ========================================
pip install python-dotenv==1.0.1
if errorlevel 1 (
    echo FAILED: python-dotenv
    pause
)
echo.

echo ========================================
echo Installing packages (8 of 10): click
echo ========================================
pip install click==8.1.7
if errorlevel 1 (
    echo FAILED: click
    pause
)
echo.

echo ========================================
echo Installing packages (9 of 10): rich
echo ========================================
pip install rich==13.9.4
if errorlevel 1 (
    echo FAILED: rich
    pause
)
echo.

echo ========================================
echo Installing packages (10 of 10): streamlit
echo ========================================
echo (This one is large and may take 2-3 minutes)
pip install streamlit==1.32.2
if errorlevel 1 (
    echo FAILED: streamlit
    echo.
    echo Streamlit is a large package. Try:
    echo 1. Check internet connection
    echo 2. Try: pip install --no-cache-dir streamlit
    echo 3. Try: pip install streamlit (without version)
    pause
)
echo.

REM Create directories
echo Creating directories...
if not exist "output" mkdir output
if not exist "settings" mkdir settings
echo.

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo If all packages installed successfully,
echo you can now run START.bat
echo.
echo If any package failed, check TROUBLESHOOTING.md
echo.
pause
