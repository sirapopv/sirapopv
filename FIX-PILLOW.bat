@echo off
REM Fix for Pillow Installation Issue
REM "failed building wheel for Pillow"

title Pillow Installation Fix

echo ========================================
echo   Pillow Installation Fix
echo ========================================
echo.
echo This will fix the "failed building wheel
echo for Pillow" error.
echo.
pause

REM Activate virtual environment
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run SETUP-SIMPLE.bat first.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo.
echo ========================================
echo   Method 1: Installing Pre-built Wheel
echo ========================================
echo.
echo Upgrading pip and wheel...
python -m pip install --upgrade pip wheel setuptools
echo.

echo Installing Pillow with pre-built binary...
echo.
python -m pip install --upgrade Pillow
if not errorlevel 1 (
    echo.
    echo ========================================
    echo   SUCCESS! Pillow installed!
    echo ========================================
    echo.
    echo Now installing remaining packages...
    echo.

    REM Install other packages
    pip install youtube-transcript-api==0.6.2
    pip install yt-dlp==2024.8.6
    pip install google-generativeai==0.8.3
    pip install gtts==2.5.4
    pip install pyyaml==6.0.2
    pip install python-dotenv==1.0.1
    pip install click==8.1.7
    pip install rich==13.9.4
    pip install streamlit==1.32.2

    echo.
    echo ========================================
    echo   All packages installed!
    echo ========================================
    echo.
    echo You can now run START.bat
    echo.
    pause
    exit /b 0
)

echo.
echo Method 1 failed. Trying alternative methods...
echo.

echo ========================================
echo   Method 2: Installing without version
echo ========================================
echo.
python -m pip install Pillow --no-cache-dir
if not errorlevel 1 (
    echo SUCCESS with Method 2!
    goto :install_rest
)

echo.
echo ========================================
echo   Method 3: Using unofficial wheels
echo ========================================
echo.
echo Pillow needs Visual C++ build tools.
echo.
echo SOLUTIONS:
echo.
echo Solution 1 (Recommended):
echo   Install Visual C++ Build Tools:
echo   https://visualstudio.microsoft.com/visual-cpp-build-tools/
echo   - Download "Build Tools for Visual Studio"
echo   - Run installer
echo   - Select "Desktop development with C++"
echo   - Install (takes 5-10 minutes)
echo   - After installation, run this script again
echo.
echo Solution 2 (Faster):
echo   Download pre-compiled Pillow wheel from:
echo   https://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
echo   - Find your Python version (python --version)
echo   - Download matching .whl file
echo   - Then run: pip install downloaded_file.whl
echo.
echo Solution 3 (Alternative):
echo   Use Pillow-SIMD (faster version):
echo   pip install Pillow-SIMD
echo.
pause
exit /b 1

:install_rest
echo Installing remaining packages...
pip install youtube-transcript-api==0.6.2
pip install yt-dlp==2024.8.6
pip install google-generativeai==0.8.3
pip install gtts==2.5.4
pip install pyyaml==6.0.2
pip install python-dotenv==1.0.1
pip install click==8.1.7
pip install rich==13.9.4
pip install streamlit==1.32.2

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
pause
