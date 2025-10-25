
# HackingTool PowerShell Installer for Windows

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  HackingTool Windows Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[*] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = & python --version 2>&1
    Write-Host "[+] $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "[X] Python is not installed!" -ForegroundColor Red
    Write-Host "[!] Please install Python 3.8+ from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check pip
Write-Host "[*] Checking pip installation..." -ForegroundColor Yellow
try {
    $pipVersion = & python -m pip --version 2>&1
    Write-Host "[+] pip found" -ForegroundColor Green
} catch {
    Write-Host "[!] Installing pip..." -ForegroundColor Yellow
    & python -m ensurepip --upgrade
}

# Upgrade pip
Write-Host "[*] Upgrading pip..." -ForegroundColor Yellow
& python -m pip install --upgrade pip | Out-Null

# Install requirements
Write-Host "[*] Installing Python dependencies..." -ForegroundColor Yellow
if (-not (Test-Path "requirements.txt")) {
    Write-Host "[X] requirements.txt not found!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

& python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "[X] Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "[+] Dependencies installed successfully" -ForegroundColor Green

# Create tools directory
Write-Host "[*] Setting up tools directory..." -ForegroundColor Yellow
$toolsDir = Join-Path $env:USERPROFILE "hackingtool_tools"
if (-not (Test-Path $toolsDir)) {
    New-Item -ItemType Directory -Path $toolsDir | Out-Null
}
$toolsDir | Out-File -FilePath ".hackingtool_path.txt" -Encoding utf8
Write-Host "[+] Tools directory created at $toolsDir" -ForegroundColor Green

# Installation complete
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "To start HackingTool Web Application:" -ForegroundColor Cyan
Write-Host "  1. Run: python app.py" -ForegroundColor White
Write-Host "  2. Open: http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "For terminal mode, run: python hackingtool.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "[!] Note: Some tools may have limited functionality on Windows" -ForegroundColor Yellow
Write-Host "[!] For best results, use WSL (Windows Subsystem for Linux)" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to exit"
