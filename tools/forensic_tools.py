
# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection


class AndroidForensics(HackingTool):
    TITLE = "Android Forensics (ADB)"
    DESCRIPTION = "Android Debug Bridge for mobile forensics over USB"
    RUN_COMMANDS = [
        "echo '=== ANDROID FORENSICS OVER USB ==='; echo ''; "
        "echo 'ANDROID DEBUG BRIDGE (USB):'; "
        "echo '  adb devices                    - List connected devices'; "
        "echo '  adb shell                      - Access device shell'; "
        "echo '  adb pull /path/to/file        - Copy file from device'; "
        "echo '  adb install app.apk           - Install an APK on the device'; "
        "echo ''; "
        "echo 'LIMITATIONS:'; "
        "echo '  ⚠️  Phone must have ADB debugging enabled (developer mode)'; "
        "echo '  ⚠️  Most data is encrypted without device unlock'; "
        "echo '  ⚠️  Physical access needed for USB connection'; "
        "echo 'Type commands above or press Ctrl+C to exit';"
    ]


class iOSForensics(HackingTool):
    TITLE = "iOS Forensics (iPhone/iPad)"
    DESCRIPTION = "iOS device forensics using libimobiledevice (iPhone 12 compatible)"
    RUN_COMMANDS = [
        "echo '=== iOS FORENSICS OVER USB ==='; echo ''; "
        "echo 'LIBIMOBILEDEVICE COMMANDS:'; "
        "echo '  ideviceinfo                    - Get device information'; "
        "echo '  ideviceinfo -k ProductVersion  - Get iOS version'; "
        "echo '  ideviceinfo -k DeviceName      - Get device name'; "
        "echo '  idevicesyslog                  - View system logs'; "
        "echo '  idevicecrashreport -e .        - Extract crash reports'; "
        "echo '  idevicebackup2 backup ./backup - Create device backup'; "
        "echo '  idevicescreenshot screenshot.png - Take screenshot'; "
        "echo ''; "
        "echo 'LIMITATIONS:'; "
        "echo '  ⚠️  Device must be unlocked and trust this computer'; "
        "echo '  ⚠️  Most data requires device to be paired'; "
        "echo '  ⚠️  Jailbreak provides more access but voids warranty'; "
        "echo '  ⚠️  iOS 12+ has additional security restrictions'; "
        "echo ''; "
        "echo 'IMPORTANT: For iPhone 12, make sure to:'; "
        "echo '  1. Connect via USB cable'; "
        "echo '  2. Unlock the device'; "
        "echo '  3. Tap Trust when prompted'; "
        "echo ''; "
        "echo 'Type commands above or press Ctrl+C to exit';"
    ]


class iOSListDevices(HackingTool):
    TITLE = "📱 List Connected iOS Devices"
    DESCRIPTION = "Show all connected iPhone/iPad devices"
    RUN_COMMANDS = [
        "echo '🔍 Checking for connected iOS devices...'; "
        "echo ''; "
        "if command -v idevice_id >/dev/null 2>&1; then "
        "  idevice_id -l || echo '⚠️  No devices found. Make sure:'; "
        "  echo '   1. Your iPhone is connected via USB'; "
        "  echo '   2. Device is unlocked'; "
        "  echo '   3. You tapped Trust on the device'; "
        "else "
        "  echo '❌ libimobiledevice is not installed!'; "
        "  echo ''; "
        "  echo '⚠️  IMPORTANT: iOS forensics tools require:'; "
        "  echo '   1. libimobiledevice installed on the system'; "
        "  echo '   2. Physical USB connection to an iOS device'; "
        "  echo '   3. This typically works on local machines, not cloud IDEs'; "
        "  echo ''; "
        "  echo '💡 To install on a local Linux machine:'; "
        "  echo '   sudo apt-get install libimobiledevice-utils'; "
        "  echo ''; "
        "  echo '📱 For Replit (cloud environment):'; "
        "  echo '   These tools cannot access USB devices remotely.'; "
        "  echo '   Download this project and run it locally instead.'; "
        "fi"
    ]


class iOSDeviceInfo(HackingTool):
    TITLE = "📋 Get Full Device Details"
    DESCRIPTION = "Display complete device information"
    RUN_COMMANDS = [
        "if command -v ideviceinfo >/dev/null 2>&1; then "
        "  ideviceinfo || echo '⚠️  Unable to connect. Ensure device is connected, unlocked, and trusted.'; "
        "else "
        "  echo '❌ libimobiledevice not installed. Run this tool locally with: sudo apt-get install libimobiledevice-utils'; "
        "fi"
    ]


class iOSDeviceName(HackingTool):
    TITLE = "📱 Get Device Name"
    DESCRIPTION = "Show the device name"
    RUN_COMMANDS = ["ideviceinfo -k DeviceName"]


class iOSVersion(HackingTool):
    TITLE = "📱 Get iOS Version"
    DESCRIPTION = "Display the iOS version"
    RUN_COMMANDS = ["ideviceinfo -k ProductVersion"]


class iOSSerialNumber(HackingTool):
    TITLE = "🔢 Get Serial Number"
    DESCRIPTION = "Display device serial number"
    RUN_COMMANDS = ["ideviceinfo -k SerialNumber"]


class iOSUDID(HackingTool):
    TITLE = "🆔 Get UDID"
    DESCRIPTION = "Display Unique Device Identifier"
    RUN_COMMANDS = ["ideviceinfo -k UniqueDeviceID"]


class iOSPairDevice(HackingTool):
    TITLE = "🔗 Pair Device"
    DESCRIPTION = "Establish pairing with iOS device"
    RUN_COMMANDS = ["idevicepair pair"]


class iOSCreateBackup(HackingTool):
    TITLE = "💾 Create Device Backup"
    DESCRIPTION = "Create full backup to ./ios_backup folder"
    RUN_COMMANDS = ["idevicebackup2 backup ./ios_backup"]


class iOSScreenshot(HackingTool):
    TITLE = "📸 Take Screenshot"
    DESCRIPTION = "Capture screenshot and save as screenshot.png"
    RUN_COMMANDS = ["idevicescreenshot screenshot.png && echo 'Screenshot saved as screenshot.png'"]


class iOSSystemLogs(HackingTool):
    TITLE = "📊 View System Logs"
    DESCRIPTION = "View real-time system logs (Press Ctrl+C to stop)"
    RUN_COMMANDS = ["idevicesyslog"]


class iOSCrashReports(HackingTool):
    TITLE = "💥 Extract Crash Reports"
    DESCRIPTION = "Extract crash reports to ./crashes folder"
    RUN_COMMANDS = ["mkdir -p ./crashes && idevicecrashreport -e ./crashes && echo 'Crash reports extracted to ./crashes'"]


class iOSDiagnostics(HackingTool):
    TITLE = "🔍 Run Diagnostics"
    DESCRIPTION = "Run device diagnostics"
    RUN_COMMANDS = ["idevicediagnostics diagnostics"]


class iOSListApps(HackingTool):
    TITLE = "📱 List Installed Apps"
    DESCRIPTION = "Show all installed applications"
    RUN_COMMANDS = ["ideviceinstaller -l"]


class iOSCapabilities(HackingTool):
    TITLE = "ℹ️ Forensic Capabilities"
    DESCRIPTION = "Show what data can be extracted without jailbreak"
    RUN_COMMANDS = [
        "echo ''; "
        "echo '🔍 FORENSIC ANALYSIS CAPABILITIES (NO JAILBREAK):'; "
        "echo '  ✓ SMS/iMessage history (from backup)'; "
        "echo '  ✓ Call logs and voicemail'; "
        "echo '  ✓ Contacts and calendar'; "
        "echo '  ✓ Photos and videos'; "
        "echo '  ✓ Safari browsing history'; "
        "echo '  ✓ Notes and reminders'; "
        "echo '  ✓ App data (for apps allowing backup)'; "
        "echo '  ✓ Health and fitness data'; "
        "echo '  ✓ Location history'; "
        "echo '  ✓ System logs and crash reports'; "
        "echo '  ✓ Network configuration'; "
        "echo '  ✓ Device settings and preferences'; "
        "echo '';"
    ]


class iOSRequirements(HackingTool):
    TITLE = "⚠️ Requirements & Limitations"
    DESCRIPTION = "Show requirements and what cannot be accessed"
    RUN_COMMANDS = [
        "echo ''; "
        "echo '⚠️  REQUIREMENTS:'; "
        "echo '  1. Device must be UNLOCKED'; "
        "echo '  2. Tap TRUST when computer pairing prompt appears'; "
        "echo '  3. USB cable connection required'; "
        "echo '  4. Device passcode may be needed for backups'; "
        "echo '  5. libimobiledevice-utils must be installed'; "
        "echo ''; "
        "echo '🔍 ENVIRONMENT CHECK:'; "
        "if command -v idevice_id >/dev/null 2>&1; then "
        "  echo '  ✓ libimobiledevice is installed'; "
        "  device_count=$(idevice_id -l 2>/dev/null | wc -l); "
        "  if [ $device_count -gt 0 ]; then "
        "    echo \"  ✓ $device_count iOS device(s) detected\"; "
        "  else "
        "    echo '  ⚠️  No iOS devices detected'; "
        "  fi; "
        "else "
        "  echo '  ❌ libimobiledevice NOT installed'; "
        "  echo '  📥 Install with: sudo apt-get install libimobiledevice-utils'; "
        "fi; "
        "echo ''; "
        "echo '☁️  REPLIT CLOUD LIMITATION:'; "
        "echo '  These tools require direct USB access to iOS devices.'; "
        "echo '  Cloud IDEs like Replit cannot access USB devices.'; "
        "echo '  💡 Download and run this project on your local machine.'; "
        "echo ''; "
        "echo '🚫 WHAT YOU CANNOT ACCESS (without jailbreak):'; "
        "echo '  ✗ Full filesystem root access'; "
        "echo '  ✗ System partition files'; "
        "echo '  ✗ Encrypted app containers'; "
        "echo '  ✗ Keychain passwords (encrypted)'; "
        "echo '  ✗ Active memory dump'; "
        "echo '  ✗ Low-level system hooks'; "
        "echo '';"
    ]


class iOSNonJailbreakForensics(HackingToolsCollection):
    TITLE = "iOS Non-Jailbreak Forensics Suite"
    DESCRIPTION = "Complete iOS forensics toolkit for iPhone 12 and other iOS devices - NO jailbreak required"
    TOOLS = [
        iOSListDevices(),
        iOSDeviceInfo(),
        iOSDeviceName(),
        iOSVersion(),
        iOSSerialNumber(),
        iOSUDID(),
        iOSPairDevice(),
        iOSCreateBackup(),
        iOSScreenshot(),
        iOSSystemLogs(),
        iOSCrashReports(),
        iOSDiagnostics(),
        iOSListApps(),
        iOSCapabilities(),
        iOSRequirements()
    ]


class Autopsy(HackingTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Digital forensics platform"
    INSTALL_COMMANDS = [
        "sudo apt-get update",
        "sudo apt-get install -y autopsy"
    ]
    RUN_COMMANDS = ["sudo autopsy"]
    PROJECT_URL = "https://www.sleuthkit.org/autopsy/"


class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic Tools"
    DESCRIPTION = "Collection of digital forensic tools for Android, iOS, and disk analysis"
    TOOLS = [
        AndroidForensics(),
        iOSForensics(),
        # iOS Non-Jailbreak Tools (flattened for web interface)
        iOSListDevices(),
        iOSDeviceInfo(),
        iOSDeviceName(),
        iOSVersion(),
        iOSSerialNumber(),
        iOSUDID(),
        iOSPairDevice(),
        iOSCreateBackup(),
        iOSScreenshot(),
        iOSSystemLogs(),
        iOSCrashReports(),
        iOSDiagnostics(),
        iOSListApps(),
        iOSCapabilities(),
        iOSRequirements(),
        Autopsy()
    ]
