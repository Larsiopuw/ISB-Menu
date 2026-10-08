param([switch]$Remove)
$ErrorActionPreference='Stop'
$isbShortcut=Join-Path ([Environment]::GetFolderPath('Startup')) 'ISB Media Bridge.lnk'
if ($Remove) {
    if (Test-Path -LiteralPath $isbShortcut) { Remove-Item -LiteralPath $isbShortcut }
    Write-Output 'ISB Media Bridge: Autostart entfernt.'
    return
}
$isbSource=Join-Path $PSScriptRoot 'ISBMediaBridge.exe'
if (-not (Test-Path -LiteralPath $isbSource)) { throw 'ISBMediaBridge.exe muss neben diesem Skript liegen.' }
$isbInstall=Join-Path $env:LOCALAPPDATA 'ISBMenu'
$isbExecutable=Join-Path $isbInstall 'ISBMediaBridge.exe'
New-Item -ItemType Directory -Path $isbInstall -Force | Out-Null
if ($isbSource -ne $isbExecutable) { Copy-Item -LiteralPath $isbSource -Destination $isbExecutable -Force }
$isbShell=New-Object -ComObject WScript.Shell
$isbLink=$isbShell.CreateShortcut($isbShortcut)
$isbLink.TargetPath=$isbExecutable
$isbLink.WorkingDirectory=$isbInstall
$isbLink.Description='ISB Menu: lokale Windows-Musikverbindung'
$isbLink.WindowStyle=7
$isbLink.Save()
$isbClient=New-Object Net.Sockets.TcpClient
try {
    $isbConnect=$isbClient.ConnectAsync('127.0.0.1',8766)
    $isbReachable=$isbConnect.Wait(500) -and $isbClient.Connected
} catch { $isbReachable=$false } finally { $isbClient.Dispose() }
if (-not $isbReachable) { Start-Process -FilePath $isbExecutable -WindowStyle Hidden }
Write-Output 'ISB Media Bridge: Autostart bei Windows-Anmeldung aktiviert.'
# -- by Larsiopuw
