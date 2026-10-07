# Windows-Musikplayer · ISB 2.6.0

1. `ISBMediaBridge.exe` starten. Sie läuft ohne zusätzliches Fenster im Hintergrund.
2. Spotify oder einen Browser mit Medienwiedergabe öffnen.
3. Im ISB-Menü den Tab **Musik** öffnen. Titel, Künstler, Cover, Position und verfügbare Player erscheinen automatisch. Über die Player-Buttons lässt sich eine Quelle auswählen; **Automatisch** verwendet wieder die Windows-Auswahl.

Die Bridge verwendet Windows-Mediensteuerung und den Windows-Lautstärkemixer. Pause/Weiter, vorheriger/nächster Titel und das Verschieben der Position sind verfügbar, wenn der ausgewählte Player diese Befehle bereitstellt. Einige Browser-Videos bieten keine Titelwechsel. App-Lautstärke ist verfügbar, sobald Windows eine passende Audiositzung bereitstellt; sie betrifft bei YouTube die Browser-App und damit gegebenenfalls mehrere Tabs. Spotify muss dafür gegebenenfalls zuerst wiedergegeben haben.

Die Verbindung bleibt lokal auf `127.0.0.1:8766`; Browser-Webseiten werden abgewiesen. Das persönliche Verbindungstoken wird ausschließlich in `ISBMenu-media-bridge.json` im Executor-Workspace gespeichert. Diese Datei nicht weitergeben. Das Paket enthält kein persönliches Token.

Real wird automatisch erkannt. Für einen anderen Executor die EXE mit `--client-workspace "C:\Pfad\zum\Executor\workspace"` starten. Ein anderer Port ist für die fertige Lua-Fassung nicht vorgesehen.

Zum Beenden im Windows-Task-Manager ausschließlich **ISBMediaBridge.exe** beenden. Es werden keine Autostarts oder geplanten Aufgaben angelegt. Nach einem Windows-Neustart die Bridge erneut starten. Das Roblox-Menü ist weiterhin ohne Bridge verwendbar; Roblox-Audio-IDs bleiben als zusätzliche Möglichkeit vorhanden.

Quellcode und festgelegte Python-Abhängigkeiten sind enthalten. Zum eigenen Build unter Windows: Abhängigkeiten aus `ISBMediaBridge-requirements.txt` sowie PyInstaller installieren und `pyinstaller --onefile --noconsole --collect-all winrt --collect-all comtypes --collect-submodules pycaw ISBMediaBridge.py` ausführen.

<!-- -- by Larsiopuw -->
