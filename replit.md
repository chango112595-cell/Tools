# HackingTool - All-in-One Cybersecurity Tools Collection

## Overview
This is a Python-based cybersecurity tools collection that provides a comprehensive menu-driven interface for various penetration testing and security assessment tools. The project was originally created by Z4nzu and provides access to tools for information gathering, vulnerability assessment, phishing attacks, forensics, and more.

**Current Status**: Web application ready - Easy-to-use interface for all tools
**Last Updated**: October 25, 2025

## Recent Changes
- **2025-10-25**: Created automated installation programs
  - Built **install.py** - Cross-platform Python installer with colorful UI
  - Built **install_hackingtool.sh** - Bash installer for Linux/macOS with virtual environment setup
  - Created comprehensive **INSTALL.md** documentation with troubleshooting guide
  - Updated README.md with modern installation instructions
  - Both installers feature:
    - Dependency checking (Python, pip, system tools)
    - Virtual environment creation
    - Automatic requirements installation
    - Tools directory setup
    - Port availability checking
    - Clear success/error messaging with colors
    - Completion messages with usage instructions

- **2025-10-25**: Debugged and fixed all application issues
  - Fixed missing favicon.ico route (eliminated 404 errors)
  - Resolved all 13 LSP type checking errors in app.py
  - Added proper type annotations (typing.Dict, typing.Any) for Flask request handling
  - Fixed Flask-SocketIO type issues with request.sid and socketio.emit() parameters
  - Added null checks for API request parameters (category_idx, tool_idx)
  - Updated socketio.emit() from 'room' to 'to' parameter for compatibility
  - Verified all dependencies in requirements.txt are present
  - Confirmed application runs without errors and all features work correctly

- **2025-10-12**: Created modern web application with interactive terminal popups
  - Built Flask web app with responsive design and visual interface
  - **Added interactive terminal popups** using xterm.js and WebSocket (Flask-SocketIO)
  - **Implemented real-time bidirectional terminal I/O** for tool interaction
  - Added PTY (pseudo-terminal) support for authentic terminal emulation
  - Implemented secure session-based command execution (prevents RCE vulnerabilities)
  - Fixed tool execution to support both RUN_COMMANDS and custom run() methods
  - Added proper error handling with finally blocks to maintain server stability
  - Implemented success/failure tracking for accurate API responses
  - Fixed menu display formatting issue in terminal version
  - Corrected missing closing bracket in menu item display (line 162 in core.py)
  - **Added 9 new professional forensic tools:**
    - Volatility 3 (memory forensics - RAM analysis, malware detection)
    - TestDisk & PhotoRec (data recovery - 480+ file formats)
    - Scalpel (file carving from disk images)
    - Chkrootkit (rootkit detection)
    - Lynis (security auditing and compliance)
    - iOS Device Tools (libimobiledevice - backup, file access, logs)
    - APKtool (Android APK decompilation and analysis)
    - Androguard (advanced Android malware/forensics analysis)
    - scrcpy (Android screen mirroring and recording)
  
- **2025-09-10**: Project imported from GitHub and configured for Replit
  - Fixed Python typing import issue in core.py (added missing 'Any' and 'Union' imports)
  - Corrected type annotation from `List[Any[...]]` to `List[Union[HackingTool, HackingToolsCollection]]`
  - Installed Python 3.11 and required dependencies (boxes, flask, lolcat, requests)
  - Installed system dependencies (figlet, boxes, php, curl, xdotool, wget)
  - Configured workflow for terminal application with console output
  - Pre-configured installation path to bypass first-run prompt

## User Preferences
- Terminal-based interface preferred (no web interface)
- Interactive menu system for tool selection and management
- All tools installed in designated directory structure

## Project Architecture

### Structure
- `hackingtool.py` - Main entry point and application launcher
- `core.py` - Core classes and framework for tools (HackingTool, HackingToolsCollection)
- `tools/` - Directory containing all individual tool implementations
- `requirements.txt` - Python dependencies
- `images/` - Screenshots and demo images

### Key Components
1. **HackingTool Class**: Base class for individual security tools with install/run capabilities
2. **HackingToolsCollection Class**: Container class for organizing groups of tools
3. **AllTools Class**: Main collection containing all available tools
4. **Interactive Menu System**: Console-based navigation and tool selection

### Tool Categories
- Anonymously Hiding Tools (AnonSurf, Multitor)
- Information Gathering Tools (nmap, reconnaissance tools)
- Wordlist Generator Tools
- Wireless Attack Tools
- SQL Injection Tools
- Phishing Attack Tools
- Web Attack Tools
- Post Exploitation Tools
- Forensic Tools
- Payload Creation Tools
- Exploit Frameworks
- Reverse Engineering Tools
- DDOS Attack Tools
- Remote Administration Tools (RAT)
- XSS Attack Tools
- Steganography Tools
- Other Tools (misc utilities)

### Workflow Configuration
- **Name**: HackingTool Web App
- **Command**: `python3 app.py`
- **Output Type**: Webview (browser interface on port 5000)
- **Status**: Running and accessible via web browser

## Usage Instructions

### Web Application (Recommended)
1. **Open the Webview** tab to access the visual interface
2. **Browse Categories**: Click on any category to see available tools
3. **Search Tools**: Use the search bar to quickly find specific tools
4. **Install & Run**: Click the Install button first, then Run to use a tool
5. **Interactive Terminal**: Running a tool opens a fully interactive terminal popup where you can type commands and see real-time output
6. **Get Info**: Click the Info button to visit the tool's GitHub page

### Terminal Mode (Alternative)
1. Run `python3 hackingtool.py` in the Console tab for text-based interface
2. The background workflow has been pre-configured with a default tool installation path

### First-Time Setup
- Path configuration has been preset to `/home/runner/hackingtool/` to avoid blocking prompts
- On first run, the application will create necessary directories
- Navigate through the interactive menu system to access various tools
- Each tool category provides installation and execution options
- Tools are installed on-demand in the specified directory

### Replit Environment Setup
- **Pre-installed Tools**: Major security tools are now installed via Nix packages:
  - Forensics: sleuthkit (Autopsy CLI), binwalk, foremost, steghide, exiftool
  - Network: nmap, wireshark, aircrack-ng, nikto
  - Password: hashcat, john, hydra
  - Penetration: metasploit, sqlmap
  - Mobile: android-tools (ADB for device forensics)
- **No sudo required**: Tools are installed through Replit's Nix package system
- **Interactive Command Reference**: Tools now show usage guides when run
- Some tools may have limited functionality in the cloud environment due to network restrictions
- Additional tools can be installed on-demand through the web interface

## Technical Notes
- Requires Python 3.11+
- Uses system commands for tool execution
- Designed primarily for Linux environments
- Some tools may require additional system permissions
- Interactive terminal interface - not suitable for headless operation

## Security Considerations
- This is an educational/professional security testing toolkit
- Should only be used on systems you own or have permission to test
- Many tools are designed for penetration testing and security auditing
- Always follow ethical hacking guidelines and legal requirements