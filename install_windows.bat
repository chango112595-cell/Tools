
@echo off
setlocal enabledelayedexpansion

:: HackingTool Windows Installer
echo ========================================
echo   HackingTool Windows Installer
echo ========================================
echo.

:: Check Python
echo [*] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python is not installed!
    echo [!] Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)
echo [+] Python found

:: Check pip
echo [*] Checking pip installation...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [X] pip is not installed!
    echo [!] Installing pip...
    python -m ensurepip --upgrade
)
echo [+] pip found

:: Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip

:: Install requirements
echo [*] Installing Python dependencies...
if not exist requirements.txt (
    echo [X] requirements.txt not found!
    pause
    exit /b 1
)
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo [X] Failed to install dependencies
    pause
    exit /b 1
)
echo [+] Dependencies installed successfully

:: Create tools directory
echo [*] Setting up tools directory...
set TOOLS_DIR=%USERPROFILE%\hackingtool_tools
if not exist "%TOOLS_DIR%" mkdir "%TOOLS_DIR%"
echo %TOOLS_DIR% > .hackingtool_path.txt
echo [+] Tools directory created at %TOOLS_DIR%

:: Installation complete
echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo To start HackingTool Web Application:
echo   1. Run: python app.py
echo   2. Open: http://localhost:5000
echo.
echo For terminal mode, run: python hackingtool.py
echo.
echo [!] Note: Some tools may have limited functionality on Windows
echo [!] For best results, use WSL (Windows Subsystem for Linux)
echo.
pause
