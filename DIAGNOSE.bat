@echo off
REM Diagnostic Script - Finds out why setup fails
REM This window will NEVER close automatically

echo ========================================
echo   DIAGNOSTIC TOOL
echo   Finding out what's wrong...
echo ========================================
echo.

REM Test 1: Check if we're in the right folder
echo [Test 1/6] Checking if we're in the right folder...
if exist "requirements.txt" (
    echo OK: requirements.txt found
) else (
    echo ERROR: requirements.txt NOT found!
    echo You need to run this from the project folder.
    echo.
    echo Current folder:
    cd
    echo.
    goto :end
)
echo.

REM Test 2: Check Python
echo [Test 2/6] Checking Python installation...
python --version 2>&1
if errorlevel 1 (
    echo ERROR: Python is NOT installed or NOT in PATH!
    echo.
    echo Solutions:
    echo 1. Install Python from: https://www.python.org/downloads/
    echo 2. During installation, CHECK "Add Python to PATH"
    echo 3. After installing, RESTART your computer
    echo 4. Try this diagnostic again
    echo.
    goto :end
) else (
    echo OK: Python is installed
)
echo.

REM Test 3: Check Python version
echo [Test 3/6] Checking Python version...
python -c "import sys; print('Python version:', sys.version); exit(0 if sys.version_info >= (3, 8) else 1)" 2>&1
if errorlevel 1 (
    echo ERROR: Python version is too old!
    echo You need Python 3.8 or newer.
    echo Download from: https://www.python.org/downloads/
    echo.
    goto :end
) else (
    echo OK: Python version is compatible
)
echo.

REM Test 4: Check pip
echo [Test 4/6] Checking pip...
python -m pip --version 2>&1
if errorlevel 1 (
    echo ERROR: pip is NOT working!
    echo.
    echo Trying to install pip...
    python -m ensurepip --default-pip
    if errorlevel 1 (
        echo FAILED to install pip!
        echo Please reinstall Python with pip included.
        goto :end
    ) else (
        echo OK: pip installed successfully
    )
) else (
    echo OK: pip is working
)
echo.

REM Test 5: Check internet connection
echo [Test 5/6] Checking internet connection...
ping -n 1 pypi.org >nul 2>&1
if errorlevel 1 (
    echo WARNING: Cannot reach pypi.org
    echo Check your internet connection.
    echo.
) else (
    echo OK: Internet connection works
)
echo.

REM Test 6: Check write permissions
echo [Test 6/6] Checking write permissions...
echo test > test_write.tmp 2>&1
if exist test_write.tmp (
    del test_write.tmp
    echo OK: Can write to this folder
) else (
    echo ERROR: Cannot write to this folder!
    echo Solution: Run as Administrator
    echo Right-click this script and select "Run as Administrator"
    echo.
    goto :end
)
echo.

REM All tests passed
echo ========================================
echo   ALL TESTS PASSED!
echo ========================================
echo.
echo Your system is ready for installation.
echo.
echo Next step: Try running SETUP-SIMPLE.bat
echo (I'll create this file for you)
echo.
goto :end

:end
echo ========================================
echo Press any key to close this window...
echo ========================================
pause >nul
