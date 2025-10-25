#!/bin/bash

# HackingTool Installation Script
# Automated installer for the HackingTool Web Application

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║    🔐  HackingTool Installer                             ║
║    All-in-One Cybersecurity Tools Collection             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Function to print colored messages
print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[i]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   print_warning "This script should not be run as root for security reasons."
   print_info "Please run as a normal user. Some commands will use sudo when needed."
   exit 1
fi

print_info "Starting installation process..."
echo ""

# Check Python version
print_info "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_success "Python $PYTHON_VERSION found"
else
    print_error "Python 3 is not installed!"
    print_info "Please install Python 3.8 or higher and try again."
    exit 1
fi

# Check if pip is installed
print_info "Checking pip installation..."
if command -v pip3 &> /dev/null; then
    print_success "pip3 found"
else
    print_error "pip3 is not installed!"
    print_info "Installing pip3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Create virtual environment (optional but recommended)
print_info "Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_warning "Virtual environment already exists"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source venv/bin/activate
print_success "Virtual environment activated"

# Upgrade pip
print_info "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
print_success "pip upgraded"

# Install Python dependencies
print_info "Installing Python dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    print_success "Python dependencies installed"
else
    print_error "requirements.txt not found!"
    exit 1
fi

# Check for system dependencies
print_info "Checking system dependencies..."

DEPS_TO_INSTALL=()

# Check for common tools
command -v git &> /dev/null || DEPS_TO_INSTALL+=("git")
command -v curl &> /dev/null || DEPS_TO_INSTALL+=("curl")
command -v wget &> /dev/null || DEPS_TO_INSTALL+=("wget")

if [ ${#DEPS_TO_INSTALL[@]} -gt 0 ]; then
    print_warning "Missing system dependencies: ${DEPS_TO_INSTALL[*]}"
    print_info "Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y "${DEPS_TO_INSTALL[@]}"
    print_success "System dependencies installed"
else
    print_success "All system dependencies are installed"
fi

# Create tools installation directory
print_info "Creating tools directory..."
TOOLS_DIR="$HOME/hackingtool_tools"
if [ ! -d "$TOOLS_DIR" ]; then
    mkdir -p "$TOOLS_DIR"
    print_success "Tools directory created at $TOOLS_DIR"
else
    print_success "Tools directory already exists at $TOOLS_DIR"
fi

# Store the path for the app
echo "$TOOLS_DIR" > .hackingtool_path.txt
print_success "Installation path configured"

# Check if port 5000 is available
print_info "Checking if port 5000 is available..."
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    print_warning "Port 5000 is already in use!"
    print_info "You may need to stop other services or configure a different port."
else
    print_success "Port 5000 is available"
fi

# Installation complete
echo ""
echo -e "${GREEN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║    ✓  Installation Complete!                             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

print_info "To start HackingTool Web Application:"
echo ""
echo -e "  ${YELLOW}1.${NC} Activate the virtual environment (if not already active):"
echo -e "     ${BLUE}source venv/bin/activate${NC}"
echo ""
echo -e "  ${YELLOW}2.${NC} Start the web server:"
echo -e "     ${BLUE}python3 app.py${NC}"
echo ""
echo -e "  ${YELLOW}3.${NC} Open your browser and navigate to:"
echo -e "     ${BLUE}http://localhost:5000${NC}"
echo ""
print_warning "Educational/Professional Use Only - Always get proper authorization"
echo ""
print_info "For terminal mode, run: ${BLUE}python3 hackingtool.py${NC}"
echo ""
