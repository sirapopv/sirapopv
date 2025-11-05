@echo off
REM Complete Windows Installation Fix
REM For when Pillow and Streamlit fail to build

title Complete Windows Fix

echo ========================================
echo   COMPLETE WINDOWS INSTALLATION FIX
echo ========================================
echo.
echo This fixes "failed building wheel" errors
echo for Pillow, Streamlit, and other packages.
echo.
echo This will:
echo - Upgrade all build tools
echo - Use pre-built binaries
echo - Install compatible versions
echo.
pause

REM Check Python
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

REM Create/use venv
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo.
echo ========================================
echo   Step 1: Upgrading Build Tools
echo ========================================
echo.
python -m pip install --upgrade pip
python -m pip install --upgrade wheel setuptools
python -m pip cache purge
echo Done!
echo.

echo ========================================
echo   Step 2: Installing Core Packages
echo   (These usually have pre-built wheels)
echo ========================================
echo.

echo [1/10] youtube-transcript-api...
pip install --no-cache-dir youtube-transcript-api
echo.

echo [2/10] yt-dlp...
pip install --no-cache-dir yt-dlp
echo.

echo [3/10] google-generativeai...
pip install --no-cache-dir google-generativeai
echo.

echo [4/10] gtts...
pip install --no-cache-dir gtts
echo.

echo [5/10] pyyaml...
pip install --no-cache-dir pyyaml
echo.

echo [6/10] python-dotenv...
pip install --no-cache-dir python-dotenv
echo.

echo [7/10] click...
pip install --no-cache-dir click
echo.

echo [8/10] rich...
pip install --no-cache-dir rich
echo.

echo ========================================
echo   Step 3: Installing Pillow
echo   (Often problematic on Windows)
echo ========================================
echo.

echo Trying to install Pillow...
pip install --no-cache-dir --prefer-binary Pillow

if errorlevel 1 (
    echo.
    echo Pillow failed. Trying older version...
    pip install Pillow==9.5.0

    if errorlevel 1 (
        echo.
        echo [WARNING] Pillow installation failed!
        echo.
        echo The app will work WITHOUT Pillow, but:
        echo - Cannot generate custom thumbnails
        echo - Will use placeholder images instead
        echo.
        echo To fix later: Install Visual C++ Build Tools
        echo https://aka.ms/vs/17/release/vs_BuildTools.exe
        echo.
        set /p continue="Continue without Pillow? (y/n): "
        if /i not "%continue%"=="y" (
            echo Installation cancelled.
            pause
            exit /b 1
        )
        echo Continuing without Pillow...
    ) else (
        echo Pillow 9.5.0 installed successfully!
    )
) else (
    echo Pillow installed successfully!
)
echo.

echo ========================================
echo   Step 4: Installing Streamlit
echo   (Large package, may take 3-5 minutes)
echo ========================================
echo.

echo [9/10] streamlit...
echo This may take several minutes, please wait...
echo.

pip install --no-cache-dir --prefer-binary streamlit

if errorlevel 1 (
    echo.
    echo Streamlit failed with standard method.
    echo Trying alternative approach...
    echo.

    REM Try installing streamlit dependencies first
    echo Installing Streamlit dependencies first...
    pip install --no-cache-dir altair
    pip install --no-cache-dir blinker
    pip install --no-cache-dir cachetools
    pip install --no-cache-dir packaging
    pip install --no-cache-dir pandas
    pip install --no-cache-dir protobuf
    pip install --no-cache-dir pyarrow
    pip install --no-cache-dir requests
    pip install --no-cache-dir tornado
    pip install --no-cache-dir watchdog

    echo.
    echo Now trying Streamlit again...
    pip install --no-cache-dir streamlit

    if errorlevel 1 (
        echo.
        echo ========================================
        echo   STREAMLIT INSTALLATION FAILED
        echo ========================================
        echo.
        echo Streamlit requires Visual C++ Build Tools.
        echo.
        echo SOLUTION:
        echo.
        echo 1. Download and install:
        echo    https://aka.ms/vs/17/release/vs_BuildTools.exe
        echo.
        echo 2. During installation, select:
        echo    "Desktop development with C++"
        echo.
        echo 3. After installation completes, RESTART your computer
        echo.
        echo 4. Run this script again
        echo.
        echo.
        echo OR use the web-only version (no local install):
        echo See DEPLOYMENT.md for Railway/Render deployment
        echo.
        pause
        exit /b 1
    ) else (
        echo Streamlit installed successfully!
    )
) else (
    echo Streamlit installed successfully!
)
echo.

echo ========================================
echo   Step 5: Creating Directories
echo ========================================
if not exist "output" mkdir output
if not exist "settings" mkdir settings
echo Done!
echo.

echo ========================================
echo   Step 6: Verifying Installation
echo ========================================
echo.
echo Checking installed packages...
python -c "import youtube_transcript_api; print('✓ youtube-transcript-api')"
python -c "import yt_dlp; print('✓ yt-dlp')"
python -c "import google.generativeai; print('✓ google-generativeai')"
python -c "import gtts; print('✓ gtts')"
python -c "import PIL; print('✓ Pillow')" 2>nul || echo "✗ Pillow (optional)"
python -c "import yaml; print('✓ pyyaml')"
python -c "import dotenv; print('✓ python-dotenv')"
python -c "import click; print('✓ click')"
python -c "import rich; print('✓ rich')"
python -c "import streamlit; print('✓ streamlit')"

if errorlevel 1 (
    echo.
    echo Some imports failed. See errors above.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS! All Packages Installed!
echo ========================================
echo.
echo Your system is ready to use!
echo.
echo Next steps:
echo 1. Double-click START.bat to launch
echo 2. Get API key from: https://makersuite.google.com/app/apikey
echo 3. Enter API key in sidebar (one time)
echo 4. Start converting videos!
echo.
echo ========================================
pause
