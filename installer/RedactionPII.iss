[Setup]
AppName=Anonimyzer
AppVersion=0.0.2
DefaultDirName={pf}\RedactionPII
DefaultGroupName=Redaction PII
UninstallDisplayIcon={app}\RedactionPII.exe
Compression=lzma2
SolidCompression=yes
OutputDir=installer
OutputBaseFilename=RedactionPII_Setup

[Files]
Source: "dist\RedactionPII.exe"; DestDir: "{app}"
Source: "README.txt"; DestDir: "{app}"; Flags: isreadme

[Icons]
Name: "{group}\Redaction PII"; Filename: "{app}\RedactionPII.exe"
Name: "{commondesktop}\Redaction PII"; Filename: "{app}\RedactionPII.exe"

[Run]
Filename: "{app}\RedactionPII.exe"; Description: "Launch Redaction PII"; Flags: nowait postinstall skipifsilent