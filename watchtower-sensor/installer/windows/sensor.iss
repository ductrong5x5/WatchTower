[Setup]
AppName=Watchtower Sensor
AppVersion=0.1
WizardStyle=modern
DefaultDirName={autopf}\Watchtower Sensor
DefaultGroupName=Watchtower Sensor
UninstallDisplayIcon={app}\sensor.exe
Compression=lzma2
SolidCompression=yes
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
OutputBaseFilename=WatchtowerSensorInstall

[Files]
Source: "..\..\target\release\sensor.exe"; DestDir: "{app}"
Source: "config.json"; DestDir: "{app}"

[Icons]
Name: "{group}\Watchtower Sensor"; Filename: "{app}\sensor.exe"

[Run]
Filename: "notepad.exe"; Parameters: "{app}\config.json"
Filename: "{app}\sensor.exe"; Flags: nowait postinstall

[Registry]
Root: HKLM; Subkey: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "WatchtowerSensor"; ValueData: """{group}\Watchtower Sensor.lnk"""; Flags: uninsdeletevalue
