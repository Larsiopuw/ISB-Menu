# Windows-Musikplayer · ISB 2.6.24

1. `ISBMediaBridge.exe` starten. Sie läuft ohne zusätzliches Fenster im Hintergrund.
2. Spotify oder einen Browser mit Medienwiedergabe öffnen.
3. Im ISB-Menü den Tab **Musik** öffnen. Titel, Künstler, Cover, Position und verfügbare Player erscheinen automatisch. Über die Player-Buttons lässt sich eine Quelle auswählen; **Automatisch** verwendet wieder die Windows-Auswahl.

Die Bridge verwendet Windows-Mediensteuerung und den Windows-Lautstärkemixer. Pause/Weiter, vorheriger/nächster Titel und das Verschieben der Position sind verfügbar, wenn der ausgewählte Player diese Befehle bereitstellt. Einige Browser-Videos bieten keine Titelwechsel. App-Lautstärke ist verfügbar, sobald Windows eine passende Audiositzung bereitstellt; sie betrifft bei YouTube die Browser-App und damit gegebenenfalls mehrere Tabs. Spotify muss dafür gegebenenfalls zuerst wiedergegeben haben.

Die Verbindung bleibt lokal auf `127.0.0.1:8766`; Browser-Webseiten werden abgewiesen. Die optionale YouTube-Erweiterung verwendet ein separates persönliches Token und kann ausschließlich YouTube-Mediendaten und zugehörige Steuerbefehle austauschen. Das persönliche Verbindungstoken wird ausschließlich in `ISBMenu-media-bridge.json` im Executor-Workspace gespeichert. Diese Datei nicht weitergeben. Das Paket enthält kein persönliches Token.

Real wird automatisch erkannt. Für einen anderen Executor die EXE mit `--client-workspace "C:\Pfad\zum\Executor\workspace"` starten. Ein anderer Port ist für die fertige Lua-Fassung nicht vorgesehen.

Zum Beenden im Windows-Task-Manager ausschließlich **ISBMediaBridge.exe** beenden. Für automatischen Start bei Windows-Anmeldung einmal ISBMediaBridge-Autostart.ps1 ausführen. Ohne diese ausdrückliche Einrichtung nach einem Windows-Neustart die Bridge erneut starten. Mit -Remove entfernt das Skript die Autostart-Verknüpfung. Es werden keine geplanten Aufgaben angelegt. Das Roblox-Menü ist weiterhin ohne Bridge verwendbar; Roblox-Audio-IDs bleiben als zusätzliche Möglichkeit vorhanden.

Quellcode und festgelegte Python-Abhängigkeiten sind enthalten. Zum eigenen Build unter Windows: Abhängigkeiten aus `ISBMediaBridge-requirements.txt` sowie PyInstaller installieren und `pyinstaller --onefile --noconsole --collect-all winrt --collect-all comtypes --collect-submodules pycaw ISBMediaBridge.py` ausführen.

## YouTube in Opera verbinden

Die normale Windows-Verbindung kann YouTubes eigene Stummschaltung und Live-DVR-Zeitleiste nicht auslesen. Dafür ist die enthaltene Erweiterung **ISB YouTube Player** erforderlich.

1. ISBMediaBridge.exe zusammen mit dem Ordner ISB-YouTube speichern. Einmal `ISBMediaBridge.exe --prepare-browser` ausführen. Bei der mitgelieferten EXE ist der Ordner auch eingebettet.
2. In Opera `opera://extensions` öffnen, **Entwicklermodus** aktivieren und **Entpackte Erweiterung laden** wählen. Den Ordner `%LOCALAPPDATA%\ISBMenu\ISB-YouTube` auswählen.
3. Den YouTube-Tab neu laden. Im ISB-Musikplayer erscheint **YouTube** als Quelle; bei passendem Windows-Titel wird sie automatisch verwendet.

Die Erweiterung hat ausschließlich Zugriff auf YouTube und die lokale Bridge, sendet nichts an externe Server und liest keine Kontodaten oder den Browserverlauf. Den persönlich vorbereiteten Ordner und `youtube-connection.json` nicht weitergeben. Die veröffentlichten Dateien enthalten kein Token. Zum Entfernen die Erweiterung in Opera löschen; die Windows-Bridge funktioniert weiter.

Bei YouTube regelt Player-Lautstärke das aktuelle Video. Erhöhen über 0 entstummt es. Der zusätzliche Knopf schaltet YouTubes eigene Stummschaltung direkt. Der Balken zeigt das tatsächlich verfügbare Rückspulfenster; ±10 Sekunden und Zur Live-Position funktionieren nur bei angebotenem DVR. Ohne DVR ist Spulen deaktiviert. Ein Rückspulfenster ist nicht automatisch die gesamte Stream-Laufzeit; diese erscheint nur bei einem von YouTube gelieferten Startdatum. Opera kann Hintergrund-Tabs drosseln; bei ausbleibender Bestätigung wird ein verständlicher Hinweis angezeigt.

<!-- -- by Larsiopuw -->
