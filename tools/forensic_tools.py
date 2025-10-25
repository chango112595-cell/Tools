
# coding=utf-8
import platform
from core import HackingTool
from core import HackingToolsCollection

IS_WINDOWS = platform.system() == 'Windows'

class AndroidForensics(HackingTool):
    TITLE = "Android Forensics (ADB)"
    DESCRIPTION = "Android Debug Bridge for mobile forensics over USB"
    
    def __init__(self):
        if IS_WINDOWS:
            self.INSTALL_COMMANDS = [
                "echo 'Installing ADB for Windows...'",
                "echo 'Please download and install Android Platform Tools from:'",
                "echo 'https://developer.android.com/tools/releases/platform-tools'",
                "echo ''",
                "echo 'Or install via Chocolatey:'",
                "echo 'choco install adb'",
                "echo ''",
                "echo 'After installation, add to PATH and restart terminal'"
            ]
        else:
            self.INSTALL_COMMANDS = [
                "sudo apt-get update",
                "sudo apt-get install -y android-tools-adb android-tools-fastboot"
            ]
        
        super().__init__()
    
    RUN_COMMANDS = [
        "echo '=== ANDROID FORENSICS OVER USB ==='; echo ''; "
        "echo 'ANDROID DEBUG BRIDGE (USB):'; "
        "echo '  adb devices                    - List connected devices'; "
        "echo '  adb shell                      - Access device shell'; "
        "echo '  adb pull /path/to/file .       - Copy file from device'; "
        "echo '  adb push file.txt /sdcard/     - Copy file to device'; "
        "echo '  adb install app.apk            - Install an APK'; "
        "echo '  adb logcat                     - View device logs'; "
        "echo ''; "
        "echo 'WINDOWS USERS:'; "
        "echo '  1. Enable USB Debugging on Android device'; "
        "echo '  2. Connect via USB'; "
        "echo '  3. Accept USB debugging prompt on device'; "
        "echo ''; "
        "echo 'LIMITATIONS:'; "
        "echo '  ⚠️  Phone must have ADB debugging enabled'; "
        "echo '  ⚠️  USB drivers required on Windows'; "
        "echo 'Type commands above or press Ctrl+C to exit';"
    ]


class iOSForensicsWindows(HackingTool):
    TITLE = "iOS Forensics (Windows Compatible)"
    DESCRIPTION = "iOS device forensics using iTunes backup on Windows"
    
    INSTALL_COMMANDS = [
        "echo 'Installing iTunes and backup tools for Windows...'",
        "echo ''",
        "echo 'REQUIRED SOFTWARE:'",
        "echo '  1. iTunes (from Microsoft Store or Apple)'",
        "echo '  2. iBackup Viewer (https://www.imactools.com/iphonebackupviewer/)'",
        "echo '  3. Or iMazing (https://imazing.com/)'",
        "echo ''",
        "echo 'Python-based alternative:'",
        "pip install iphone-backup-decrypt",
        "echo ''",
        "echo 'Installation complete!'"
    ]
    
    RUN_COMMANDS = [
        "echo '=== iOS FORENSICS ON WINDOWS ==='; echo ''; "
        "echo 'METHOD 1 - iTunes Backup (No Jailbreak):'; "
        "echo '  1. Connect iPhone via USB'; "
        "echo '  2. Open iTunes and create backup'; "
        "echo '  3. Backup location:'; "
        "echo '     %APPDATA%\\Apple Computer\\MobileSync\\Backup\\'; "
        "echo ''; "
        "echo 'METHOD 2 - iBackup Viewer:'; "
        "echo '  1. Install from https://www.imactools.com/iphonebackupviewer/'; "
        "echo '  2. Open and browse iTunes backups'; "
        "echo '  3. Extract SMS, Photos, Contacts, etc.'; "
        "echo ''; "
        "echo 'METHOD 3 - Python Tools:'; "
        "echo '  pip install iphone-backup-decrypt'; "
        "echo '  Then use: iphone_backup_decrypt'; "
        "echo ''; "
        "echo 'WHAT YOU CAN ACCESS:'; "
        "echo '  ✓ SMS/iMessage history'; "
        "echo '  ✓ Call logs'; "
        "echo '  ✓ Contacts'; "
        "echo '  ✓ Photos and videos'; "
        "echo '  ✓ Safari history'; "
        "echo '  ✓ App data (some apps)'; "
        "echo '  ✓ Notes'; "
        "echo ''; "
        "echo 'Press any key to continue...'; read -n 1;"
    ]


class WindowsForensics(HackingTool):
    TITLE = "Windows System Forensics"
    DESCRIPTION = "Forensic tools for Windows systems"
    
    RUN_COMMANDS = [
        "echo '=== WINDOWS FORENSICS TOOLS ==='; echo ''; "
        "echo 'BUILT-IN WINDOWS COMMANDS:'; "
        "echo ''; "
        "echo 'System Information:'; "
        "echo '  systeminfo                     - Full system details'; "
        "echo '  wmic bios get serialnumber     - Get BIOS serial'; "
        "echo '  wmic computersystem get name   - Get computer name'; "
        "echo ''; "
        "echo 'Network Forensics:'; "
        "echo '  ipconfig /all                  - Network configuration'; "
        "echo '  arp -a                         - ARP table'; "
        "echo '  netstat -ano                   - Active connections'; "
        "echo '  nbtstat -A [IP]                - NetBIOS info'; "
        "echo ''; "
        "echo 'Process & Service Analysis:'; "
        "echo '  tasklist /v                    - Running processes'; "
        "echo '  tasklist /svc                  - Services'; "
        "echo '  wmic process list full         - Detailed processes'; "
        "echo ''; "
        "echo 'User & Security:'; "
        "echo '  net user                       - Local users'; "
        "echo '  net localgroup administrators  - Admin users'; "
        "echo '  wevtutil qe Security /f:text   - Security events'; "
        "echo ''; "
        "echo 'File Analysis:'; "
        "echo '  dir /s /b                      - List all files'; "
        "echo '  findstr /s /i \"password\" *.*   - Search for text'; "
        "echo ''; "
        "echo 'Registry Forensics:'; "
        "echo '  reg query HKLM\\Software       - Query registry'; "
        "echo ''; "
        "echo 'Press any key to continue...'; read -n 1;"
    ]


class AutopsyWindows(HackingTool):
    TITLE = "Autopsy (Windows Version)"
    DESCRIPTION = "Digital forensics platform for Windows"
    
    INSTALL_COMMANDS = [
        "echo 'Installing Autopsy for Windows...'",
        "echo ''",
        "echo 'MANUAL INSTALLATION REQUIRED:'",
        "echo '  1. Download Autopsy from:'",
        "echo '     https://www.autopsy.com/download/'",
        "echo '  2. Run the Windows installer'",
        "echo '  3. Follow installation wizard'",
        "echo ''",
        "echo 'REQUIREMENTS:'",
        "echo '  - Windows 10 or 11'",
        "echo '  - 8GB+ RAM recommended'",
        "echo '  - Java Runtime Environment'",
        "echo ''",
        "echo 'After installation, launch from Start Menu'"
    ]
    
    RUN_COMMANDS = [
        "echo 'Opening Autopsy...'",
        "echo ''",
        "echo 'If installed, Autopsy should be in:'",
        "echo 'Start Menu -> Autopsy'",
        "echo ''",
        "echo 'Or run from command line:'",
        "echo 'C:\\Program Files\\Autopsy-[version]\\bin\\autopsy64.exe'",
        "echo ''",
        "echo 'FEATURES:'",
        "echo '  - Timeline Analysis'",
        "echo '  - File System Analysis'",
        "echo '  - Keyword Search'",
        "echo '  - Email Analysis'",
        "echo '  - Registry Analysis'",
        "echo '  - Web Artifacts'",
        "echo ''",
        "start autopsy64.exe 2>nul || echo 'Autopsy not found. Please install it first.'"
    ]


class FTKImagerWindows(HackingTool):
    TITLE = "FTK Imager (Disk Imaging)"
    DESCRIPTION = "Free disk imaging and forensic tool for Windows"
    
    INSTALL_COMMANDS = [
        "echo 'Installing FTK Imager...'",
        "echo ''",
        "echo 'DOWNLOAD:'",
        "echo '  https://accessdata.com/product-download/ftk-imager-version-4-5'",
        "echo ''",
        "echo 'INSTALLATION:'",
        "echo '  1. Download the installer'",
        "echo '  2. Run as Administrator'",
        "echo '  3. Follow installation wizard'",
        "echo ''",
        "echo 'FREE FOR COMMERCIAL USE!'"
    ]
    
    RUN_COMMANDS = [
        "echo '=== FTK IMAGER ==='; echo ''; "
        "echo 'CAPABILITIES:'; "
        "echo '  - Create disk images (E01, DD, AFF)'"; "
        "echo '  - Preview files on drives'"; "
        "echo '  - Extract files from images'"; "
        "echo '  - Create forensic reports'"; "
        "echo '  - Calculate hash values'"; "
        "echo '';"
    ]


class VolatilityWindows(HackingTool):
    TITLE = "Volatility (Memory Forensics)"
    DESCRIPTION = "Memory forensics framework - Windows compatible"
    
    INSTALL_COMMANDS = [
        "pip install volatility3",
        "echo ''",
        "echo 'Volatility 3 installed!'",
        "echo ''",
        "echo 'For memory dumps, you can use:'",
        "echo '  - DumpIt (https://github.com/thimbleweed/All-In-USB/)'",
        "echo '  - FTK Imager'",
        "echo '  - Magnet RAM Capture'"
    ]
    
    RUN_COMMANDS = [
        "echo '=== VOLATILITY MEMORY FORENSICS ==='; echo ''; "
        "echo 'BASIC USAGE:'; "
        "echo '  vol -f memory.dmp windows.info        - Get system info'; "
        "echo '  vol -f memory.dmp windows.pslist      - List processes'; "
        "echo '  vol -f memory.dmp windows.pstree      - Process tree'; "
        "echo '  vol -f memory.dmp windows.cmdline     - Command lines'; "
        "echo '  vol -f memory.dmp windows.netstat     - Network connections'; "
        "echo '  vol -f memory.dmp windows.filescan    - Scan for files'; "
        "echo ''; "
        "echo 'MEMORY ACQUISITION TOOLS:'; "
        "echo '  - DumpIt: https://www.magnetforensics.com/resources/dumpit/';"
    ]


class WiresharkWindows(HackingTool):
    TITLE = "Wireshark (Network Forensics)"
    DESCRIPTION = "Network protocol analyzer for Windows"
    
    INSTALL_COMMANDS = [
        "echo 'Installing Wireshark for Windows...'",
        "echo ''",
        "echo 'DOWNLOAD:'",
        "echo '  https://www.wireshark.org/download.html'",
        "echo ''",
        "echo 'Or install via Chocolatey:'",
        "echo '  choco install wireshark'",
        "echo ''",
        "echo 'IMPORTANT: Install WinPcap or Npcap when prompted!'"
    ]
    
    RUN_COMMANDS = [
        "echo '=== WIRESHARK NETWORK FORENSICS ==='; echo ''; "
        "echo 'LAUNCHING WIRESHARK...'; "
        "start wireshark 2>nul || echo 'Wireshark not found. Please install it first.'; "
        "echo '';"
    ]


class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic Tools"
    DESCRIPTION = "Digital forensic tools - Windows Compatible"
    
    def __init__(self):
        if IS_WINDOWS:
            self.TOOLS = [
                AndroidForensics(),
                iOSForensicsWindows(),
                WindowsForensics(),
                AutopsyWindows(),
                FTKImagerWindows(),
                VolatilityWindows(),
                WiresharkWindows()
            ]
        else:
            # Original Linux tools
            self.TOOLS = [
                AndroidForensics(),
                iOSForensicsWindows(),
                WindowsForensics(),
                AutopsyWindows(),
                FTKImagerWindows(),
                VolatilityWindows(),
                WiresharkWindows()
            ]
        
        super().__init__()
