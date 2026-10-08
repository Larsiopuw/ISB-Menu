$ErrorActionPreference = 'Stop'
$isbCandidate = Join-Path $PSScriptRoot 'ISBMediaBridge-v2.6.24.exe'
if (-not (Test-Path -LiteralPath $isbCandidate)) { throw 'Die neue EXE muss neben diesem Update-Skript liegen.' }
if ((Get-FileHash -LiteralPath $isbCandidate -Algorithm SHA256).Hash -ne 'F280964A4061B4D4A313A257F5A4E770D895DF6A6E7D9E2903BE3F0280B1ADBB') {
    throw 'Die EXE stimmt nicht mit dem geprüften Release überein.'
}
$isbDestination = Join-Path $env:LOCALAPPDATA 'ISBMenu/ISBMediaBridge.exe'
$isbPrevious = Join-Path $PSScriptRoot 'ISBMediaBridge.exe'
$isbKnownPaths = @([IO.Path]::GetFullPath($isbDestination), [IO.Path]::GetFullPath($isbPrevious))
foreach ($isbProcess in @(Get-Process ISBMediaBridge -ErrorAction SilentlyContinue)) {
    if ($isbProcess.Path -and [IO.Path]::GetFullPath($isbProcess.Path) -in $isbKnownPaths) {
        Stop-Process -Id $isbProcess.Id -Force -ErrorAction SilentlyContinue
    }
}
New-Item -ItemType Directory -Path (Split-Path $isbDestination) -Force | Out-Null
Copy-Item -LiteralPath $isbCandidate -Destination $isbDestination -Force
Start-Process -FilePath $isbDestination -ArgumentList '--prepare-browser' -WindowStyle Hidden -Wait
$isbStartup = Join-Path ([Environment]::GetFolderPath('Startup')) 'ISB Media Bridge.lnk'
if (Test-Path -LiteralPath $isbStartup) {
    $isbShell = New-Object -ComObject WScript.Shell
    $isbShortcut = $isbShell.CreateShortcut($isbStartup)
    $isbShortcut.TargetPath = $isbDestination
    $isbShortcut.WorkingDirectory = Split-Path $isbDestination
    $isbShortcut.Save()
}
Start-Process -FilePath $isbDestination -WindowStyle Hidden
Write-Host 'Bridge aktualisiert. In Opera den Ordner für die entpackte Erweiterung laden:'
Write-Host (Join-Path $env:LOCALAPPDATA 'ISBMenu/ISB-YouTube')
# -- by Larsiopuw
