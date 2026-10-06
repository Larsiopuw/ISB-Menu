# ISB Menu 2.0 · by Larsiopuw

Universelles Roblox-Clientmenü mit kompaktem Dock, schwebenden Panels, einheitlichen Heroicons und animierten Übergängen. Die Gestaltung orientiert sich an den bereitgestellten Videos: dunkles Graphit, klare Typografie und zurückhaltende Farbakzente. Der Name ist vom Imperialen Sicherheitsbüro inspiriert.

![Interaktive Designvorschau mit Beispieldaten](ISB-Vorschau.png)

## Starten

```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/main/ISBMenu.lua"))()
-- by Larsiopuw
```

Das Repository ist öffentlich; der Quellcode bleibt lesbar. Der Aufruf lädt den aktuellen Stand von main. Alternativ ISBMenu.lua vollständig direkt ausführen. ISBMenu-Loader.lua lädt eine lokale Datei aus dem Workspace-Ordner des Executors; ISBMenu-GitHub-Loader.lua lädt die GitHub-Version mit Fehlerprüfung.

**RightShift** oder der ISB-Button öffnet und schließt das Menü. Der aktive Dock-Button klappt das Panel ein. Unter **Einstellungen → Tasten** eine Taste durch Anklicken und anschließendes Drücken vergeben; Escape bricht ab. **Einstellungen → Allgemein → Beenden** entfernt das Menü und setzt seine verwalteten Änderungen zurück. Erneutes Ausführen ersetzt die alte Instanz.

## Funktionen

| Bereich | Enthalten |
| --- | --- |
| Start | Spielname, Spielerzahl, Freunde im Server, Freundestatistik, erkannter Executor und Version, Dauer der Hub-Sitzung, öffentliche/private Sitzung |
| Bewegung | Fliegen, Noclip, Mehrfachsprung, Speed, Jump, Fluggeschwindigkeit, FOV, Reset, Respawn, Rejoin, Serverhop |
| Spieler | Suche, Profilbilder, Beobachten und Kamerarückkehr, lokale Positionsänderung zum Spieler |
| Server | Öffentliche Server des aktuellen Place, Spielerzahl, Ping/FPS soweit geliefert, Sortierung, Cursor-Paginierung, Beitreten und Join-Script kopieren |
| Darstellung | Highlights, Namen und Entfernung, helle Umgebung, Schatten und Sichtfeld |
| Skripte | ScriptBlox, RoScripts, RScripts; Suche, Anbieterwechsel, Ergebnisse, Detailquelltext, Kopieren und explizite Ausführung; lokale Lua-Dateien hinzufügen |
| Musik/Zeit | Roblox-Audio-IDs, Warteschlange, Vor/Zurück, Pause/Weiter, Stop, Lautstärke, Timer und Stoppuhr mit Aktivitäts-Widget |
| Einstellungen | Neutral/Blue/Mint/Amber, Tastenerfassung, weniger Animationen, Hintergrundunschärfe, Executor-Fähigkeiten und Protokoll |
| Voice | Berechtigungsstatus, AudioDeviceInput stummschalten, Reconnect soweit unterstützt |
| Hinweise/Favoriten | Gestapelte Meldungen, Freund-beigetreten-Hinweis, Hinweise für konfigurierte Staff-User-IDs, lokal gespeicherte Favoriten |

Fliegen nutzt LinearVelocity und AlignOrientation: WASD bzw. Roblox-Bewegungssteuerung horizontal, Space nach oben und linkes Strg nach unten. Touch-Geräte erhalten Hoch-/Runter-Buttons. Funktionen werden nach Respawn wieder angewendet. Individuelle Charaktercontroller und Server-Skripte können lokale Änderungen überschreiben; die Universalbasis verwendet Standard-Roblox-Objekte.

## Skriptanbieter

- **ScriptBlox:** dokumentierte Such- und Detail-API, keine Zugangsdaten nötig.
- **RoScripts:** liest öffentliche Suchergebnisse und deren Raw-Script-Adresse aus dem beobachteten HTML-Format. Lokale Paginierung mit zwölf Einträgen. Website-Änderungen können eine Anpassung erfordern.
- **RScripts:** aktuelle v1-API. Ein persönlicher rsc_live_…-Key und ein HTTP-Provider mit Header-Unterstützung sind nötig. Der Key gilt nur für die Hub-Sitzung und wird ausschließlich an api.rscripts.net gesendet. Keine Speicherung in Einstellungen, Logs oder Repository; kein Key ist im Projekt hinterlegt.

Die Suche führt nichts automatisch aus. Nach Auswahl zeigt das Menü den verfügbaren Quelltext; **Ausführen** startet ihn nach deinem Klick. Dieser Quelltext kann selbst ein weiterer Loader sein. Anbieterausfälle und fehlende APIs erscheinen als Fehler. ISB-Designvorschau.html demonstriert die Bedienung mit gekennzeichneten Beispieldaten und führt keine Roblox-Aktionen oder fremden Skripte aus.

## Voice, Staff und Daten

Ein garantierter **Anti-VC-Ban** ist nicht implementiert: lokale Mikrofon- oder Verbindungsänderungen verhindern keine serverseitige Sperre. Voice-Werkzeuge funktionieren nur, soweit die jeweiligen APIs verfügbar sind.

CONFIG.StaffUserIds am Anfang von ISBMenu.lua nimmt bekannte User-IDs entgegen. Eine leere Liste behauptet keine automatische Administratorerkennung. Serverregionen werden nicht erfunden. Die Sitzungsdauer zählt ab Hub-Start.

Favoriten, Akzent, Animationseinstellung, Unschärfe und Menü-Taste werden in ISBMenu-settings.json gespeichert, sofern readfile/writefile verfügbar sind. Aktive Bewegungsfunktionen starten ausgeschaltet. Die 29 Heroicons sind als PNG-Daten eingebettet und brauchen keine Icon-Downloads. writefile und getcustomasset/getsynasset ermöglichen diese Icons; ohne diese Fähigkeiten verwendet das Dock gezeichnete Ersatzsymbole. Die MIT-Lizenz der Icons liegt bei und ist im Lua-Skript enthalten.

Musik nutzt Roblox-Audioassets; die Freigaben des Spiels bestimmen deren Abspielbarkeit. Externe Skripte und eigene Erweiterungen verwalten ihre Änderungen selbst; Beenden setzt die von ISB Menu verwalteten Eigenschaften zurück.

## Eigene Aktionen

```lua
local hub = ((getgenv and getgenv()) or _G).ISBMenu
assert(hub, "ISB Menu zuerst starten")
hub.AddAction("mein-spiel-info", "Spieler", "Spiel-Info", "Eigene Erweiterung", function()
    hub.Notify("Meine eigene Aktion wurde ausgeführt.")
end)
-- by Larsiopuw
```

Eindeutige IDs und Bewegung, Spieler oder Darstellung als Kategorie verwenden. Fehler der Aktions-Callbacks werden abgefangen.

## Prüfung

- Luau 0.741: Menü und beide Loader erfolgreich kompiliert.
- 59 Assertions mit simulierter Roblox-API bestehen: Bedienung, Suche, Bewegung, Ausgangswerte, JumpHeight, Flug-/Kollisions-Cleanup, Respawn, Beleuchtung, Kamera, Spielerwechsel, Timer, Tastenerfassung, Erweiterungen, erneuter Start; zusätzlich Server-Paginierung, Anbieter-Parsing, Quelltextansicht, Kopieren und Ausführung erst nach Klick.
- ScriptBlox und RoScripts anhand abgerufener Antworten untersucht. Tests verwenden diese als Fixtures und führen deren fremden Code nicht aus. RScripts anhand offizieller API-Dokumentation angebunden; kein echter persönlicher Key für einen Live-Test vorhanden.
- Designvorschau im Browser visuell und interaktiv geprüft. Sie belegt keine Ausführung im Roblox-Executor.
- Ein Live-Test in deinem konkreten Spiel und Executor steht aus. Mobilgeräte wurden nicht in Roblox getestet.

Referenzen: [ScriptBlox Suche](https://docs.scriptblox.com/docs/scripts/search), [RoScripts](https://roscripts.io), [RScripts API](https://rscripts.net/docs/api), [Roblox VoiceChatService](https://create.roblox.com/docs/reference/engine/classes/VoiceChatService), [Roblox TeleportService](https://create.roblox.com/docs/reference/engine/classes/TeleportService). TLMenu wurde als Vergleich gelesen; ISB Menu ist eine eigenständige Implementierung und keine vollständige Kopie aller TLMenu-Erweiterungen.

