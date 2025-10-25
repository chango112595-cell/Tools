#!/usr/bin/env python3
"""
HackingTool Python Installer
Cross-platform installation script for HackingTool
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

class Colors:
    """ANSI color codes"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

def print_banner():
    """Print installation banner"""
    banner = f"""{Colors.BLUE}
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║    🔐  HackingTool Installer (Python)                    ║
║    All-in-One Cybersecurity Tools Collection             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
{Colors.NC}"""
    print(banner)

def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}[✓]{Colors.NC} {message}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}[✗]{Colors.NC} {message}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.BLUE}[i]{Colors.NC} {message}")

def print_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}[!]{Colors.NC} {message}")

def check_python_version():
    """Check if Python version is compatible"""
    print_info("Checking Python version...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8+ is required. You have Python {version.major}.{version.minor}")
        return False
    
    print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_pip():
    """Check if pip is installed"""
    print_info("Checking pip installation...")
    
    try:
        import pip
        print_success("pip is installed")
        return True
    except ImportError:
        print_error("pip is not installed!")
        print_info("Please install pip and try again.")
        return False

def install_requirements():
    """Install Python requirements"""
    print_info("Installing Python dependencies...")
    
    requirements_file = Path("requirements.txt")
    
    if not requirements_file.exists():
        print_error("requirements.txt not found!")
        return False
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print_success("Python dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False

def create_tools_directory():
    """Create directory for tools installation"""
    print_info("Setting up tools directory...")
    
    home_dir = Path.home()
    tools_dir = home_dir / "hackingtool_tools"
    
    tools_dir.mkdir(exist_ok=True)
    print_success(f"Tools directory created at {tools_dir}")
    
    # Save path configuration
    path_file = Path(".hackingtool_path.txt")
    path_file.write_text(str(tools_dir))
    print_success("Installation path configured")
    
    return tools_dir

def check_system_dependencies():
    """Check for common system dependencies"""
    print_info("Checking system dependencies...")
    
    system = platform.system()
    
    if system == "Linux":
        commands = ["git", "curl", "wget"]
        missing = []
        
        for cmd in commands:
            if not shutil.which(cmd):
                missing.append(cmd)
        
        if missing:
            print_warning(f"Missing dependencies: {', '.join(missing)}")
            print_info("Please install them using your package manager:")
            print_info(f"  sudo apt-get install {' '.join(missing)}")
            return False
        else:
            print_success("All system dependencies found")
            return True
    
    elif system == "Darwin":  # macOS
        print_info("macOS detected. Using Homebrew recommended.")
        return True
    
    elif system == "Windows":
        print_warning("Windows detected. Some tools may have limited functionality.")
        return True
    
    return True

def check_port_availability(port=5000):
    """Check if the specified port is available"""
    import socket
    
    print_info(f"Checking if port {port} is available...")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    
    if result == 0:
        print_warning(f"Port {port} is already in use!")
        print_info("You may need to stop other services or configure a different port.")
        return False
    else:
        print_success(f"Port {port} is available")
        return True

def print_completion_message():
    """Print completion message with instructions"""
    print()
    completion = f"""{Colors.GREEN}
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║    ✓  Installation Complete!                             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
{Colors.NC}"""
    print(completion)
    
    print_info("To start HackingTool Web Application:")
    print()
    print(f"  {Colors.YELLOW}1.{Colors.NC} Start the web server:")
    print(f"     {Colors.BLUE}python3 app.py{Colors.NC}")
    print()
    print(f"  {Colors.YELLOW}2.{Colors.NC} Open your browser and navigate to:")
    print(f"     {Colors.BLUE}http://localhost:5000{Colors.NC}")
    print()
    print_warning("Educational/Professional Use Only - Always get proper authorization")
    print()
    print_info(f"For terminal mode, run: {Colors.BLUE}python3 hackingtool.py{Colors.NC}")
    print()

def main():
    """Main installation function"""
    print_banner()
    print_info("Starting installation process...")
    print()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check pip
    if not check_pip():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Create tools directory
    create_tools_directory()
    
    # Check system dependencies
    check_system_dependencies()
    
    # Check port availability
    check_port_availability()
    
    # Print completion message
    print_completion_message()

if __name__ == "__main__":
    main()
