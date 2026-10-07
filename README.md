# ISB Menu 2.5.0 · by Larsiopuw

Glossy Dark: dunkles Graphit, durchscheinende Flächen, weiche Lichtkanten und ein einstellbarer Akzent. Feste Navigation unten mittig, Statusleiste sechs Pixel von der oberen rechten Spielkante entfernt.

![Rollskala in der Designvorschau mit Beispieldaten](ISB-Charakter.png)

Der Executor-Name steht jetzt zusätzlich ganz rechts in der Statusleiste. Lange Namen werden mit Auslassungspunkten gekürzt.

Benachrichtigungen stehen zwölf Pixel vom unteren rechten Bildschirmrand. Das Dock reserviert automatisch Platz über sichtbaren, erkennbaren Inventar-/Hotbar-Leisten. Nicht zugängliche oder unbekannt benannte Sonderinventare können nicht zuverlässig erkannt werden. Die Sitzungsdetails zeigen Spielname, Place-ID, Universe-ID, Serverart, Job-ID und Spiellink getrennt; Link und Server-ID sind kopierbar.

Neu in 2.4.3: Die Statusleiste wächst mit ihren Texten. Sitzungsdaten stehen in anklickbaren Kopierfeldern neben dem Roblox-Spielicon; der rohe Spiellink wird nicht zusätzlich angezeigt. Namensanzeigen nutzen kompakte Karten. FOV gibt es unter Bewegung mit eigenem Reset. Buchstabenkürzel und ihre Erfassung folgen dem Tastaturlayout (einschließlich deutschem Z/Y); bei fehlender Layout-API gilt QWERTZ als Ersatz. Freund- und Admin-Austritte werden gemeldet, erneute Admin-Prüfungen erzeugen keine doppelten Beitrittsmeldungen.

## Neu in 2.5

- Lesbarere Schrift, stärkere Statuswerte und kompakte ISB-/ISBQ-Schaltflächen. ISB schaltet das Dock, ISBQ öffnet Schnellaktionen mit den ausgerüsteten Avatar-Emotes.
- Spielersuche durchsucht ausschließlich Spieler. Freunde stehen vor erkanntem Staff, danach folgen die übrigen Spieler; Aktualisierungen erhalten die Scrollposition. Die genaue öffentliche Gruppenrolle erscheint in der Liste.
- Details: Avatar, Benutzer-ID, Accountalter, Team, Gesundheit, Beziehung, Gruppenrolle und Profil-Link. „Freund anfragen“ öffnet den Roblox-Dialog. Namenshistorie (erste zehn Einträge) und öffentliche Outfits (erste zwanzig) werden erst auf Klick geladen und zwischengespeichert. Fehler und leere Ergebnisse werden ausgewiesen.
- Speed und Jump werden bei aktivierter Funktion vor jedem Physikschritt lokal erneut angewendet. Getrennte Werte; JumpPower/JumpHeight werden unterstützt. Mehrfachsprung setzt zusätzlich einen Aufwärtsimpuls. Serverkorrekturen können weiterhin eingreifen.
- Q schaltet beim Fliegen vier Stufen: Normal 1×, Schnell 1,5×, Turbo 2× und Maximum 3× des eingestellten Flugtempos. Eine kompakte Anzeige zeigt Tempo und Stufe; deren Taste ist ebenfalls umbelegbar. Beim Schreiben greifen die Kürzel nicht.
- Anti-Void merkt sich bei Bodenkontakt die letzte sichere Position und korrigiert lokal vor Erreichen der Fallgrenze. Keine Garantie gegen serverseitigen Tod oder spezielle Spielmechaniken.
- Licht-Preset mit dezenter Farbkorrektur und Bloom; entfernt beim Ausschalten nur die selbst erzeugten Effekte.
- Einstellungen für Links/Mitte/Rechts, Größe 50–120 %, Benachrichtigungen, Sounds und Öffnen beim Start werden automatisch gespeichert, sofern der Executor Dateizugriff bietet. Auf kleinen Bildschirmen wird die Größe zusätzlich begrenzt.

Roleplay verwendet ausgerüstete Avatar-Emotes. Carry/Hug und ähnliche gemeinsame Aktionen benötigen die Unterstützung des jeweiligen Spiels. Die Vorschau ist eine Browserdarstellung mit ausdrücklich markierten Beispieldaten.

![ISBQ und Flugstufen in der Browservorschau](ISB-Schnellaktionen.png)

## Starten

```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/main/ISBMenu.lua"))()
-- by Larsiopuw
```

Öffentlicher, lesbarer Quellcode. Der Loader lädt den aktuellen Stand von main. Alternativ ISBMenu.lua vollständig ausführen. Der lokale Loader lädt die Datei; der GitHub-Loader enthält Fehlerprüfung.

| Taste | Funktion |
| --- | --- |
| M | Hauptpanel öffnen / schließen |
| K | Festes Dock einfahren / ausfahren |
| T | Mittige Skript-Schnellsuche |
| F | Fliegen an / aus |
| Z | Noclip an / aus |
| E | Highlights / ESP an / aus |
| V | Konfigurierte Laufgeschwindigkeit an / aus |
| Q | Während des Fliegens nächste Geschwindigkeitsstufe |
| Escape | Schnellsuche oder Tastenaufnahme abbrechen |

Tasten in Einstellungen anklicken und neu belegen. Doppelte Belegungen werden abgewiesen; beim Schreiben greifen die Kürzel nicht. Fenster und Dock bleiben an der in Allgemein gewählten Position verankert. Erneutes Ausführen ersetzt die vorherige Instanz.

## Änderungen in 2.4

- Neue Rollskala für Speed, Jump, Flight, FOV und Musiklautstärke. Teilstriche und Zahlen bewegen sich unter einer festen Mittelmarkierung; kein verschiebbarer Punkt und keine Fülllinie. Nach links ziehen erhöht den Wert, nach rechts verringert ihn. Der gesamte sichtbare Skalenbereich ist der Griff. Während des Ziehens pausiert das Scrollen des Panels.
- Die Zahl ist ein editierbares Feld. Eingaben oberhalb des voreingestellten Skalenbereichs sind möglich; Komma und Dezimalpunkt werden akzeptiert. Beim nächsten Ziehen kehrt der Regler in den voreingestellten Bereich zurück.
- Manuelle Bereiche: Speed/Jump/Flight 0–10.000, FOV 1–120 Grad, Lautstärke 0–1.000 Prozent. Ungültige oder nicht endliche Eingaben werden abgewiesen. Skala: Speed 8–120, Jump 20–150, Flight 5–150, FOV 40–110, Lautstärke 0–100.
- Flugbewegung mit kontinuierlicher, kritisch gedämpfter Beschleunigung und Bremsung vor dem Physikschritt. Gleiche Zielgeschwindigkeit bei unterschiedlichen Physikraten; weichere Übergänge und höhere Orientierungsresponsivität.
- Lauf-/Schrittgeräusche des eigenen Charakters werden während des Fluges gezielt stummgeschaltet; ursprüngliche Lautstärken werden beim Ausschalten, Respawn und Beenden wiederhergestellt. Auch neu angelegte Schrittgeräusche werden berücksichtigt. Andere Musik bleibt unverändert.
- F/Z/E/V schalten die Funktionen um. Alle sieben Belegungen sind in Einstellungen → Tasten änderbar und werden gespeichert. Doppelte Belegungen werden abgewiesen; Textfelder und bereits verarbeitete Eingaben lösen keine Aktionen aus.
- Ersatzzeiger aus 2.3.1 vollständig entfernt. Das Menü zeichnet keinen eigenen Mauszeiger und ändert weder MouseIcon noch MouseIconEnabled. Interaktive Text-/Bildflächen ersetzen native GuiButtons, um deren Handzeiger-Wechsel zu umgehen. Klick, Touch, Hover und Tastaturauswahl bleiben bedienbar; Fokusverlust verwirft einen begonnenen Klick.

Das gemeldete Mausflackern ist ohne Live-Client nicht reproduziert. Die überarbeitete Eingabesteuerung ist geprüft; eine vollständige Behebung auf dem betroffenen PC ist noch nicht bestätigt. Spiel- oder Executor-eigene Mausgrafiken werden nicht verändert.

## Änderungen in 2.3

- Glossy Dark mit Lichtverläufen und enthaltenen Rahmen; Akzent einstellbar.
- Hinweiskarten erscheinen nur bei geschlossenem Panel und geschlossener Schnellsuche. Bei offenen Panels reagiert nur das Dock-Symbol auf Hover.
- Statusleiste ignoriert den Roblox-GUI-Abstand und sitzt direkt oben rechts.
- Profil mit Avatar, Rolle, Kontoalter, UserId, Sammlung, Executor, Version, Place/Universe, Sitzung und Speicherstatus.
- Profilwerkzeuge zum Kopieren von Sitzungsdaten und Exportieren der Einstellungen. Owner/Admin erhalten lokale Diagnose-, Benachrichtigungs- und Erkennungswerkzeuge.
- Automatisches Speichern von Einstellungen, Tasten, Reglerwerten, Lautstärke, Erkennung, Performance, Anbieter und Favoriten.
- Skripte laden direkt beim Öffnen: Beliebt, Neu oder Favoriten. Karten mit Titel, Spiel, Aufrufen und Vorschaubild, soweit verfügbar.
- Overhead-Anbindung und zugehöriges Server-Skript entfernt.

## Funktionen

| Bereich | Enthalten |
| --- | --- |
| Start | Spiel, Spieler/Freunde, Executor, Sitzungsdauer und Rolle |
| Bewegung | Weicher kamerabezogener Flug, Noclip, Mehrfachsprung, Speed/Jump/Flight/FOV, Reset, Respawn, Rejoin, Serverhop |
| Spieler | Suche, Avatare, Beobachten, Kamerarückkehr, lokale Positionsänderung |
| Server | Öffentliche Server, Sortierung, Cursor-Seiten, Beitreten, Join-Script kopieren |
| Darstellung | Highlights, Namen/Entfernung, Tageslicht, Schatten, FOV |
| Skripte | ScriptBlox/RoScripts, Entdecken, Suche, gespeicherte Skripte, Quelltextvorschau, Kopieren, ausdrückliches Ausführen, lokale Lua-Dateien |
| Musik | Roblox-Audio-IDs, Warteschlange, Lautstärke, Pause, Timer, Stoppuhr |
| Einstellungen | Akzent, Klänge, Tasten, Performance, Erkennung, Protokoll |
| Profil | Konto-/Sitzungsdaten, Speicherstatus, Export, lokale Verwaltungswerkzeuge |

Flug: WASD, Space hoch, linke Strg runter; Touch mit Bewegungssteuerung und Höhentasten. Reset aktualisiert Spielwerte und sichtbare Regler. Freunde werden blau, öffentlich erkennbare Spiel-Admins rot markiert.

## Speicherung und Rollen

Einstellungen werden automatisch in ISBMenu-settings.json im Dateibereich des Executors gespeichert. Dafür sind readfile/writefile nötig; fehlender Dateizugriff erscheint im Profil. Skript-Favoriten speichern Metadaten, keinen fremden Quelltext. Aktive Bewegungsmodi werden beim Neustart nicht automatisch eingeschaltet.

OwnerNames enthält Larsiopuw; zusätzliche Menü-Admins stehen als numerische UserIds in CONFIG.AdminUserIds. Die Rolle steuert lokale Menüwerkzeuge und vergibt keine serverseitigen Spielrechte. Erkannte Gruppen-Admins sind davon getrennt.

## Prüfung und Grenzen

524 Assertions bestehen mit einer simulierten Roblox-API. Menü und beide Loader kompilieren mit Luau. Flugverlauf bei 30/120 Physikschritten, Geräusch-Wiederherstellung, Rollskala, direkte Zahleneingabe, alle vier Aktionskürzel und deren Speicherung wurden simuliert geprüft. Die HTML-Vorschau wurde im Browser bedient und visuell geprüft; sie zeigt Beispieldaten. **Kein Live-Test in Roblox/Executor durchgeführt.** Bewegung, Voice, Assets und Teleports hängen vom Spiel und Executor ab.

ScriptBlox nutzt die öffentliche API: Beliebt nach Aufrufen, Neu nach Aktualisierung. RoScripts nutzt öffentliche Trending-/Neu-Seiten und Such-HTML. Kein API-Key. Bei der Anbieterprüfung zu v2.3 lieferte ScriptBlox HTTP 200; der direkte RoScripts-Abruf wurde hier mit HTTP 403 blockiert. Anbieterfehler werden angezeigt; Website-Änderungen können Anpassungen erfordern. Fremder Code läuft erst nach ausdrücklichem Klick.

Vorschaubilder benötigen Dateizugriff und getcustomasset/getsynasset; PNG/JPEG werden unterstützt. Andernfalls bleibt eine gestaltete Ersatzfläche. Audio benötigt passende Asset-Freigaben. Heroicons unter beiliegender MIT-Lizenz; Interface-Klänge selbst synthetisiert.

Der experimentelle lokale Voice-Modus bietet keinen nachgewiesenen Schutz vor serverseitigen Voice-Sperren. Gruppenrollen werden anhand öffentlicher Bezeichnungen eingeordnet; versteckte oder anders benannte Rollen können fehlen. CONFIG.StaffUserIds ergänzt die Erkennung.

Erweiterungen: ISBMenu.AddAction, ISBMenu.Notify und ISBMenu.Destroy.

Designreferenz: [Apple Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/). Anbieter: [ScriptBlox](https://docs.scriptblox.com/docs/scripts/fetch), [RoScripts Trending](https://roscripts.io/trending).

<!-- -- by Larsiopuw -->
