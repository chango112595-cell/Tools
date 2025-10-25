# HackingTool Installation Guide

## 🚀 Quick Install

### Method 1: Automated Python Installer (Recommended - Cross-Platform)

```bash
python3 install.py
```

This installer will:
- ✓ Check Python version compatibility
- ✓ Verify pip installation
- ✓ Install all Python dependencies
- ✓ Set up tools directory
- ✓ Configure installation paths
- ✓ Check port availability

### Method 2: Bash Installer (Linux/macOS)

```bash
chmod +x install_hackingtool.sh
./install_hackingtool.sh
```

This installer will:
- ✓ Create and activate virtual environment
- ✓ Install system dependencies
- ✓ Install Python packages
- ✓ Configure installation paths

---

## 📋 Prerequisites

### Minimum Requirements
- **Python**: 3.8 or higher
- **pip**: Python package manager
- **Operating System**: Linux, macOS, or Windows (with limitations)
- **Disk Space**: At least 2GB free

### System Dependencies (Linux)
```bash
sudo apt-get update
sudo apt-get install -y git curl wget python3-pip
```

### System Dependencies (macOS)
```bash
brew install git curl wget python3
```

### System Dependencies (Windows)
1. **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/)
2. **Git for Windows**: Download from [git-scm.com](https://git-scm.com/download/win)
3. Ensure Python and Git are added to PATH during installation

---

---

## 💻 Windows Installation

### Method 1: PowerShell Installer (Recommended)
```powershell
# Run PowerShell as Administrator
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
powershell -ExecutionPolicy Bypass -File install_windows.ps1
```

### Method 2: Batch File Installer
```cmd
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
install_windows.bat
```

### Method 3: Python Installer
```cmd
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
python install.py
```

**Note**: Many tools are designed for Linux and may have limited functionality on Windows. For full compatibility, consider using:
- **WSL (Windows Subsystem for Linux)** - Recommended
- **VirtualBox/VMware** with Kali Linux
- **Docker** (see Docker installation section)

---

## 🔧 Manual Installation

If you prefer to install manually:

### Step 1: Clone Repository
```bash
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Installation Path
```bash
mkdir -p ~/hackingtool_tools
echo "$HOME/hackingtool_tools" > .hackingtool_path.txt
```

---

## 🌐 Running the Web Application

### Start the Web Server
```bash
python3 app.py
```

### Access the Interface
Open your browser and navigate to:
```
http://localhost:5000
```

### Features
- 🔍 **Search Tools**: Quickly find security tools
- 📦 **Easy Installation**: One-click tool installation
- 💻 **Interactive Terminal**: Run tools with real-time I/O
- 🎨 **Modern UI**: Clean, responsive design
- 🔐 **Secure**: Session-based command execution

---

## 📟 Running Terminal Mode

For the classic terminal interface:

```bash
python3 hackingtool.py
```

Navigate using the menu system to select and run tools.

---

## 🐳 Docker Installation

### Build Docker Image
```bash
docker build -t hackingtool .
```

### Run Container
```bash
docker run -it hackingtool
```

Or using docker-compose:
```bash
docker-compose up -d
```

---

## 🔒 Security Notes

⚠️ **IMPORTANT**: This tool is for **educational and professional use only**

- Always get proper authorization before testing
- Only use on systems you own or have permission to test
- Some tools may require root/administrator privileges
- Be aware of legal implications in your jurisdiction

---

## 🛠️ Troubleshooting

### Port 5000 Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process (replace PID)
kill -9 <PID>

# Or run on different port
export PORT=8080
python3 app.py
```

### Python Version Issues
```bash
# Check Python version
python3 --version

# Update Python (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3.11
```

### Missing Dependencies
```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt

# Or force reinstall
pip install --force-reinstall -r requirements.txt
```

### Permission Errors
```bash
# Install to user directory
pip install --user -r requirements.txt

# Or use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📁 Directory Structure

After installation:
```
hackingtool/
├── app.py                      # Web application
├── hackingtool.py             # Terminal application
├── core.py                    # Core framework
├── requirements.txt           # Python dependencies
├── install.py                 # Python installer
├── install_hackingtool.sh     # Bash installer
├── tools/                     # Tool modules
│   ├── anonsurf.py
│   ├── information_gathering_tools.py
│   ├── forensic_tools.py
│   └── ...
├── templates/                 # HTML templates
│   └── index.html
├── static/                    # CSS/JS assets
│   ├── css/
│   └── js/
└── ~/hackingtool_tools/       # Installed tools directory
```

---

## 🔄 Updating

### Update HackingTool
```bash
git pull origin main
pip install --upgrade -r requirements.txt
```

### Update Individual Tools
Use the web interface or terminal menu to reinstall tools.

---

## 📞 Support

For issues, questions, or contributions:
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check README.md and replit.md

---

## ⚖️ License

This project is licensed under the terms specified in the LICENSE file.

**Thanks to the original authors of all tools included in HackingTool.**
