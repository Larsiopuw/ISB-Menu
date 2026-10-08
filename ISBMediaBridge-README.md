# Optionale Windows-Musiksteuerung · ISB 2.6.26

Das Roblox-Skript allein kann Spotify und YouTube außerhalb des Spiels nicht erkennen oder bedienen. Dafür ist dieses lokale Windows-Hintergrundprogramm erforderlich. Es wird nicht durch das Lua-Menü heruntergeladen, installiert oder gestartet. Im Musik-Tab **Einrichtungsbefehl kopieren** anklicken und einmal in Windows PowerShell einfügen. Der Befehl prüft Installer und EXE, installiert für das eigene Windows-Konto und richtet den Autostart ein. Keine Administratorrechte erforderlich. Die Bridge wird sofort gestartet, sofern noch keine Verbindung läuft. Wiederholtes Ausführen verwendet dieselbe geprüfte EXE und dieselbe Autostart-Verknüpfung.

Wer kein Zusatzprogramm nutzen möchte, kann alle übrigen Menüfunktionen sowie Roblox-Audio verwenden. Eine Browser-Erweiterung wird nicht benötigt.

Bei dir eingerichteter Windows-Autostart gilt nur für deinen PC. Andere Nutzer müssten das Programm selbst einmal einrichten; eine vollständig voraussetzungslose externe Medienerkennung ist damit nicht möglich.

YouTubes eigene Stummschaltung und nicht von Windows bereitgestellte Live-Zeitdaten sind nicht steuerbar. App-Lautstärke regelt den Windows-Mixer und hebt eine Stummschaltung innerhalb der Webseite nicht auf.

1. `ISBMediaBridge.exe` starten. Sie läuft ohne zusätzliches Fenster im Hintergrund.
2. Spotify oder einen Browser mit Medienwiedergabe öffnen.
3. Im ISB-Menü den Tab **Musik** öffnen. Titel, Künstler, Cover, Position und verfügbare Player erscheinen automatisch. Über die Player-Buttons lässt sich eine Quelle auswählen; **Automatisch** verwendet wieder die Windows-Auswahl.

Die Bridge verwendet Windows-Mediensteuerung und den Windows-Lautstärkemixer. Pause/Weiter, vorheriger/nächster Titel und das Verschieben der Position sind verfügbar, wenn der ausgewählte Player diese Befehle bereitstellt. Einige Browser-Videos bieten keine Titelwechsel. App-Lautstärke ist verfügbar, sobald Windows eine passende Audiositzung bereitstellt; sie betrifft bei YouTube die Browser-App und damit gegebenenfalls mehrere Tabs. Spotify muss dafür gegebenenfalls zuerst wiedergegeben haben.

Die Verbindung bleibt lokal auf `127.0.0.1:8766`; Browser-Webseiten werden abgewiesen. Das persönliche Verbindungstoken wird ausschließlich in `ISBMenu-media-bridge.json` im Executor-Workspace gespeichert. Diese Datei nicht weitergeben. Das Paket enthält kein persönliches Token.

Real wird automatisch erkannt. Für einen anderen Executor die EXE mit `--client-workspace "C:\Pfad\zum\Executor\workspace"` starten. Ein anderer Port ist für die fertige Lua-Fassung nicht vorgesehen.

Zum Beenden im Windows-Task-Manager ausschließlich **ISBMediaBridge.exe** beenden. Für automatischen Start bei Windows-Anmeldung einmal ISBMediaBridge-Autostart.ps1 ausführen. Ohne diese ausdrückliche Einrichtung nach einem Windows-Neustart die Bridge erneut starten. Mit -Remove entfernt das Skript die Autostart-Verknüpfung. Es werden keine geplanten Aufgaben angelegt. Das Roblox-Menü ist weiterhin ohne Bridge verwendbar; Roblox-Audio-IDs bleiben als zusätzliche Möglichkeit vorhanden.

Quellcode und festgelegte Python-Abhängigkeiten sind enthalten. Zum eigenen Build unter Windows: Abhängigkeiten aus `ISBMediaBridge-requirements.txt` sowie PyInstaller installieren und `pyinstaller --onefile --noconsole --collect-all winrt --collect-all comtypes --collect-submodules pycaw ISBMediaBridge.py` ausführen.

## Andere Executor-Workspaces

Real wird automatisch erkannt. Für einen anderen Executor den geprüften Installer mit `-ClientWorkspace "C:/Pfad/zum/Executor/workspace"` ausführen. Dieses Argument wird auch in der Autostart-Verknüpfung gespeichert. Der Executor muss lokale HTTP-Anfragen und Workspace-Dateien unterstützen.

Zum Deaktivieren Win+R drücken, `shell:startup` öffnen und die Verknüpfung **ISB Media Bridge** entfernen. Eine bereits laufende Bridge kann über den Task-Manager beendet werden. Die Einrichtung bleibt erhalten, bis sie entfernt wird; eine Windows-Neuinstallation oder ein Benutzerwechsel erfordern erneute Einrichtung.

<!-- -- by Larsiopuw -->
