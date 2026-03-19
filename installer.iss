; ============================================================================
;  Salary & Goals Calculator / Calculadora de Salario & Metas
;  Inno Setup Script — v1.0 RC
;  Author  : Erick Perez
;  Released: 03/15/2026
;  Repo    : https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas
;
;  HOW TO USE THIS FILE:
;  ─────────────────────
;  STEP 1 ── Build the .exe first with PyInstaller:
;
;    pip install pyinstaller pillow reportlab
;
;    pyinstaller --onefile --windowed ^
;      --name "SalaryGoalsCalculator" ^
;      --hidden-import reportlab ^
;      --hidden-import PIL ^
;      --hidden-import PIL.ImageFont ^
;      --hidden-import PIL.ImageDraw ^
;      --collect-all reportlab ^
;      --collect-all PIL ^
;      Calculadora_Ahorro.py
;
;    Output: dist\SalaryGoalsCalculator.exe
;
;  STEP 2 ── Download & install Inno Setup 6:
;    https://jrsoftware.org/isdl.php
;
;  STEP 3 ── Open THIS file in Inno Setup IDE
;    File → Open → installer.iss → press F9 (or Build → Compile)
;
;  STEP 4 ── Collect output:
;    Output\SalaryGoalsCalculator_v1.0RC_Setup.exe
;
;  OPTIONAL: Add your own icon at assets\icon.ico
;            If icon.ico is not found, comment out AppIconFilename below.
; ============================================================================


; ─────────────────────────────────────────────────────────────────────────────
;  APP IDENTITY
; ─────────────────────────────────────────────────────────────────────────────
#define AppName        "Salary & Goals Calculator"
#define AppNameShort   "SalaryGoalsCalculator"
#define AppVersion     "1.0 RC"
#define AppVersionFile "1.0.0.0"
#define AppPublisher   "Erick Perez"
#define AppURL         "https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas"
#define AppExeName     "SalaryGoalsCalculator.exe"
#define AppCopyright   "Copyright (C) 2026 Erick Perez"
#define ReleaseDate    "2026-03-15"
#define AppDescription "Calculadora de Salario & Metas — Panama, Colombia, Mexico"


[Setup]
; ── Unique app GUID — regenerate at https://guidgenerator.com if you fork ──
AppId                    = {{A7F3C2D1-8E4B-4F9A-B6C3-D2E1F0A5B8C4}
AppName                  = {#AppName}
AppVersion               = {#AppVersion}
AppVerName               = {#AppName} {#AppVersion}
AppPublisher             = {#AppPublisher}
AppPublisherURL          = {#AppURL}
AppSupportURL            = {#AppURL}/issues
AppUpdatesURL            = {#AppURL}/releases
AppCopyright             = {#AppCopyright}
AppComments              = {#AppDescription}

; ── Paths ──────────────────────────────────────────────────────────────────
; Source .exe — adjust if your dist\ folder is elsewhere
SourceDir                = .
OutputDir                = Output
OutputBaseFilename       = {#AppNameShort}_v1.0RC_Setup

; Install location: Program Files\Salary & Goals Calculator
DefaultDirName           = {autopf}\{#AppName}
DefaultGroupName         = {#AppName}
DisableProgramGroupPage  = yes

; ── Appearance ─────────────────────────────────────────────────────────────
SetupIconFile            = assets\icon.ico
WizardStyle              = modern
WizardSizePercent        = 110
DisableWelcomePage       = no
ShowLanguageDialog       = auto

; ── Installer behavior ─────────────────────────────────────────────────────
Compression              = lzma2/ultra64
SolidCompression         = yes
InternalCompressLevel    = ultra64
LZMAUseSeparateProcess   = yes
LZMANumBlockThreads      = 4

; ── Privileges & compatibility ─────────────────────────────────────────────
PrivilegesRequired       = lowest
PrivilegesRequiredOverridesAllowed = dialog
ArchitecturesAllowed     = x64compatible
ArchitecturesInstallIn64BitMode = x64compatible

; ── Versioning (used by Windows Add/Remove Programs) ───────────────────────
VersionInfoVersion       = {#AppVersionFile}
VersionInfoCompany       = {#AppPublisher}
VersionInfoDescription   = {#AppName} {#AppVersion} Installer
VersionInfoCopyright     = {#AppCopyright}
VersionInfoProductName   = {#AppName}
VersionInfoProductVersion= {#AppVersion}

; ── Uninstaller ────────────────────────────────────────────────────────────
UninstallDisplayName     = {#AppName} {#AppVersion}
UninstallDisplayIcon     = {app}\{#AppExeName}
CreateUninstallRegKey    = yes

; ── Sign output (optional — comment out if no code-signing cert) ────────────
; SignTool = signtool sign /td sha256 /fd sha256 /tr http://timestamp.digicert.com $f


; ─────────────────────────────────────────────────────────────────────────────
;  LANGUAGES
; ─────────────────────────────────────────────────────────────────────────────
[Languages]
Name: "english";    MessagesFile: "compiler:Default.isl";         Caption: "English"
Name: "spanish";    MessagesFile: "compiler:Languages\Spanish.isl"; Caption: "Español"


; ─────────────────────────────────────────────────────────────────────────────
;  FILES TO INSTALL
; ─────────────────────────────────────────────────────────────────────────────
[Files]
; ── Main executable (built by PyInstaller --onefile) ──────────────────────
Source: "dist\{#AppExeName}";    DestDir: "{app}";  Flags: ignoreversion

; ── Documentation ─────────────────────────────────────────────────────────
Source: "README.md";             DestDir: "{app}";  Flags: ignoreversion isreadme
Source: "CHANGELOG.txt";         DestDir: "{app}";  Flags: ignoreversion

; ── License ───────────────────────────────────────────────────────────────
Source: "LICENSE";               DestDir: "{app}";  Flags: ignoreversion skipifsourcedoesntexist

; ── Optional icon asset (used for shortcuts) ──────────────────────────────
Source: "assets\icon.ico";       DestDir: "{app}";  Flags: ignoreversion skipifsourcedoesntexist


; ─────────────────────────────────────────────────────────────────────────────
;  SHORTCUTS
; ─────────────────────────────────────────────────────────────────────────────
[Icons]
; Start Menu
Name: "{group}\{#AppName}";
  Filename: "{app}\{#AppExeName}";
  IconFilename: "{app}\icon.ico";
  WorkingDir: "{app}";
  Comment: "Calculadora de Salario & Metas by Erick Perez"

; Start Menu — Uninstall
Name: "{group}\Uninstall {#AppName}";
  Filename: "{uninstallexe}";
  IconFilename: "{app}\icon.ico"

; Desktop shortcut (optional — user is prompted)
Name: "{autodesktop}\{#AppName}";
  Filename: "{app}\{#AppExeName}";
  IconFilename: "{app}\icon.ico";
  WorkingDir: "{app}";
  Comment: "Calculadora de Salario & Metas";
  Tasks: desktopicon

; Quick Launch (Windows 7 legacy — harmless on Win10/11)
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#AppName}";
  Filename: "{app}\{#AppExeName}";
  Tasks: quicklaunchicon


; ─────────────────────────────────────────────────────────────────────────────
;  TASKS (user-facing checkboxes on the "Select Additional Tasks" page)
; ─────────────────────────────────────────────────────────────────────────────
[Tasks]
Name: "desktopicon";
  Description: "{cm:CreateDesktopIcon}";
  GroupDescription: "{cm:AdditionalIcons}";
  Flags: unchecked

Name: "quicklaunchicon";
  Description: "{cm:CreateQuickLaunchIcon}";
  GroupDescription: "{cm:AdditionalIcons}";
  Flags: unchecked; onlyifdoesntexist


; ─────────────────────────────────────────────────────────────────────────────
;  REGISTRY ENTRIES
; ─────────────────────────────────────────────────────────────────────────────
[Registry]
; Register in Add/Remove Programs with extra metadata
Root: HKCU; Subkey: "Software\ErickPerez\{#AppNameShort}";
  ValueType: string; ValueName: "Version";   ValueData: "{#AppVersion}";   Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\ErickPerez\{#AppNameShort}";
  ValueType: string; ValueName: "InstallDir"; ValueData: "{app}";           Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\ErickPerez\{#AppNameShort}";
  ValueType: string; ValueName: "ReleaseDate"; ValueData: "{#ReleaseDate}"; Flags: uninsdeletekey


; ─────────────────────────────────────────────────────────────────────────────
;  RUN AFTER INSTALL
; ─────────────────────────────────────────────────────────────────────────────
[Run]
; Offer to launch immediately after install
Filename: "{app}\{#AppExeName}";
  Description: "{cm:LaunchProgram,{#AppName}}";
  Flags: nowait postinstall skipifsilent


; ─────────────────────────────────────────────────────────────────────────────
;  UNINSTALL — CLEANUP
; ─────────────────────────────────────────────────────────────────────────────
[UninstallDelete]
; Remove any log or temp files the app may have created inside its folder
Type: filesandordirs; Name: "{app}\__pycache__"
Type: filesandordirs; Name: "{app}\*.log"


; ─────────────────────────────────────────────────────────────────────────────
;  CUSTOM MESSAGES (bilingual wizard text)
; ─────────────────────────────────────────────────────────────────────────────
[CustomMessages]

; ── English ──────────────────────────────────────────────────────────────────
english.WelcomeLabel2=This will install [name/ver] on your computer.%n%n\
  Calculate your real take-home pay, plan your monthly budget, and track%n\
  savings goals — for Panama, Colombia and Mexico.%n%n\
  Released: {#ReleaseDate}%n\
  Author: {#AppPublisher}%n%n\
  It is recommended that you close all other applications before continuing.

english.FinishedHeadingLabel=Installation Complete
english.FinishedLabel={#AppName} {#AppVersion} has been successfully installed.%n%n\
  Launch the app and choose your language (English / Español) on first run.%n%n\
  Your session data is saved locally in your home folder and is never uploaded.

; ── Spanish ──────────────────────────────────────────────────────────────────
spanish.WelcomeLabel2=Este asistente instalará [name/ver] en tu computadora.%n%n\
  Calcula tu salario neto real, planifica tu presupuesto mensual y alcanza%n\
  tus metas de ahorro — para Panamá, Colombia y México.%n%n\
  Versión publicada: {#ReleaseDate}%n\
  Autor: {#AppPublisher}%n%n\
  Se recomienda cerrar todas las aplicaciones antes de continuar.

spanish.FinishedHeadingLabel=Instalación Completada
spanish.FinishedLabel={#AppName} {#AppVersion} fue instalado exitosamente.%n%n\
  Al abrir la app, elige tu idioma (English / Español) en la primera pantalla.%n%n\
  Tus datos de sesión se guardan localmente en tu carpeta de usuario y%n\
  nunca se suben a ningún servidor.


; ─────────────────────────────────────────────────────────────────────────────
;  PASCAL SCRIPT — Pre-install checks & smart upgrade detection
; ─────────────────────────────────────────────────────────────────────────────
[Code]

// ── Check for a previous installation and warn user ──────────────────────────
function InitializeSetup(): Boolean;
var
  OldVersion: String;
  Msg: String;
begin
  Result := True;

  if RegQueryStringValue(HKCU,
    'Software\ErickPerez\{#AppNameShort}',
    'Version', OldVersion) then
  begin
    if OldVersion <> '{#AppVersion}' then
    begin
      Msg := 'A previous version (' + OldVersion + ') of {#AppName} is already installed.' + #13#10 +
             'The installer will upgrade it to version {#AppVersion}.' + #13#10#13#10 +
             'Your saved sessions will not be affected.' + #13#10#13#10 +
             'Continue?';
      if MsgBox(Msg, mbConfirmation, MB_YESNO) = IDNO then
        Result := False;
    end;
  end;
end;


// ── Confirm uninstall ────────────────────────────────────────────────────────
function InitializeUninstall(): Boolean;
begin
  Result := MsgBox(
    'Are you sure you want to uninstall {#AppName} {#AppVersion}?' + #13#10#13#10 +
    'Your saved session data (~/.salary_calc_sessions.json) will NOT be deleted.',
    mbConfirmation, MB_YESNO) = IDYES;
end;


// ── After install: open GitHub releases page (optional) ──────────────────────
procedure CurStepChanged(CurStep: TSetupStep);
begin
  // Nothing automatic — user chooses to launch via [Run] checkbox above
end;
