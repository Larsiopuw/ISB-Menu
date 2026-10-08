param(
    [string]$ClientWorkspace,
    [string]$InstallDirectory = (Join-Path $env:LOCALAPPDATA 'ISBMenu'),
    [string]$StartupDirectory = [Environment]::GetFolderPath('Startup'),
    [switch]$SkipStart
)
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$isbRelease = 'ec646a9'
$isbExpectedHash = '6FE4C9FD2594A297893F7411D75A4E63A3D70E9900991CA472427C518E26621D'
$isbExecutable = Join-Path $InstallDirectory 'ISBMediaBridge.exe'
New-Item -ItemType Directory -Path $InstallDirectory -Force | Out-Null
$isbInstalled = (Test-Path -LiteralPath $isbExecutable) -and ((Get-FileHash -LiteralPath $isbExecutable -Algorithm SHA256).Hash -eq $isbExpectedHash)
if (-not $isbInstalled) {
    $isbDownload = Join-Path $InstallDirectory ('ISBMediaBridge-download-'+[Guid]::NewGuid().ToString('N')+'.exe')
    Invoke-WebRequest -UseBasicParsing -Uri ('https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/'+$isbRelease+'/ISBMediaBridge.exe') -OutFile $isbDownload -TimeoutSec 90
    if ((Get-FileHash -LiteralPath $isbDownload -Algorithm SHA256).Hash -ne $isbExpectedHash) {
        throw 'Download konnte nicht bestätigt werden. Installation abgebrochen.'
    }
    try { Move-Item -LiteralPath $isbDownload -Destination $isbExecutable -Force }
    catch { throw 'Die Bridge läuft möglicherweise bereits. ISBMediaBridge im Task-Manager beenden und den Befehl erneut ausführen.' }
}
$isbArguments = ''
if ($ClientWorkspace) {
    if ($ClientWorkspace.Contains('"')) { throw 'Ungültiger Workspace-Pfad.' }
    $isbArguments = '--client-workspace "'+[IO.Path]::GetFullPath($ClientWorkspace)+'"'
}
New-Item -ItemType Directory -Path $StartupDirectory -Force | Out-Null
$isbShortcutPath = Join-Path $StartupDirectory 'ISB Media Bridge.lnk'
$isbShell = New-Object -ComObject WScript.Shell
$isbShortcut = $isbShell.CreateShortcut($isbShortcutPath)
$isbShortcut.TargetPath = [IO.Path]::GetFullPath($isbExecutable)
$isbShortcut.WorkingDirectory = [IO.Path]::GetFullPath($InstallDirectory)
$isbShortcut.Arguments = $isbArguments
$isbShortcut.Description = 'ISB Menu: Musiksteuerung automatisch bei Windows-Anmeldung starten'
$isbShortcut.WindowStyle = 7
$isbShortcut.Save()
if (-not $SkipStart) {
    $isbClient = New-Object Net.Sockets.TcpClient
    try { $isbConnect=$isbClient.ConnectAsync('127.0.0.1',8766); $isbReachable=$isbConnect.Wait(500) -and $isbClient.Connected }
    catch { $isbReachable=$false } finally { $isbClient.Dispose() }
    if (-not $isbReachable) {
        if ($isbArguments) { Start-Process -FilePath $isbExecutable -ArgumentList $isbArguments -WindowStyle Hidden }
        else { Start-Process -FilePath $isbExecutable -WindowStyle Hidden }
    }
}
Write-Host 'ISB-Musiksteuerung eingerichtet.' -ForegroundColor Green
Write-Host 'Autostart ist für dein Windows-Konto aktiviert. Im Spiel verbindet sich das Musikmenü automatisch.'
Write-Host 'Real wird automatisch erkannt. Andere Executor-Workspaces können über -ClientWorkspace angegeben werden.'
Write-Host 'Autostart deaktivieren: Win+R, shell:startup öffnen und ISB Media Bridge entfernen.'
# -- by Larsiopuw
