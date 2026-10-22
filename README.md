# ISB Menu 2.6.83 · by Larsiopuw

## 777 Auto-Spin

Unter **Scripts → Dieses Spiel → 777 Auto-Spin** öffnen. **Auto-Spin starten** sucht eine freie, bodennahe Position am Automaten, teleportiert einmal dorthin und betätigt den normalen Spin-Prompt. Die Funktion reagiert direkt auf die Freigabe des Knopfs und sendet einen Versuch pro Freigabe, ohne zusätzliche Wartezeit. Eine Prüfung pro Frame dient als Rückfall. Das eigene Ergebnis wird beim Abschluss der Drehung übernommen. Belegte Automaten werden abgewartet; es werden keine Ergebnisse oder Gewinnchancen verändert. Es gibt keine Sieg- oder Zeitgarantie.

**Bei freigeschaltetem Titel stoppen** ist standardmäßig an. Wer 777 bereits besitzt, wird deshalb beim Start weder teleportiert noch dreht er weiter. Für weitere Drehungen kann diese Option bewusst ausgeschaltet werden. Ein bestätigtes eigenes 777 oder der entsprechende Profilfortschritt beendet die Automatik bei aktiver Option. Drehungen und letztes eigenes Ergebnis stehen kompakt in der Hauptkarte.

Der lokale AFK-Schutz ist ausschließlich während Auto-Spin aktiv und verwendet Roblox VirtualUser; es werden keine PC-weiten Tasten und keine dauerhaft deaktivierten fremden Idle-Verbindungen verwendet. Stop, Respawn, entfernte/ersetzte Automaten, Verlassen des Knopfbereichs und Fehler entfernen die eigene Idle-Verbindung. Backend-Fehler stoppen die Funktion. Der Backend-Aufruf und die Bereinigung sind live geprüft; ein kompletter 20-Minuten-Idle-Test ist nicht durchgeführt. Spiel- oder Verbindungsabbrüche können dadurch nicht ausgeschlossen werden.

Start beendet aktive Flug-/Freecam-/Quick-Action-/Piano-Steuerung, damit sich diese nicht mit der Platzierung überlagert. Danach bleibt der Charakter frei beweglich; Weglaufen stoppt die Automatik, statt ihn zurückzuziehen. Die Funktion startet nicht automatisch nach Laden oder Respawn und wird nicht als aktiv gespeichert. Sie ist an dasselbe registrierte Spiel/Place wie die drei Brettspiele gebunden und steht nach Schach, Vier gewinnt und Tic Tac Toe.

## Vier gewinnt automatisch spielen

Unter **Scripts → Dieses Spiel → Vier gewinnt** öffnen. Dieser Eintrag erscheint wie Schach und Tic Tac Toe nur für Universe `7447878628`, Place `136162036182779`. Am eigenen Tisch **Auto spielen** oder **Ein Zug** wählen. **Pause** beendet weitere Züge. Autoplay bleibt nach einer beendeten Runde am selben Tisch aktiv und setzt nach dem automatischen Reset fort. Aufstehen oder Wechsel des Charakters/Tisches beendet es. Der Start ist immer manuell; Autoplay wird nicht gespeichert.

Die Hauptkarte zeigt das 7×6-Brett, die eigene Farbe, Gewinnlinien, letzte Spalte, erreichte Suchtiefe und Stellungseinschätzung. Der Spieler liest das replizierte Echo direkt und bestätigt jeden eigenen Zug über das gesetzte Feld. Die Spielerzuordnung wird zusätzlich gegen die wirklich besetzten Tischsitze geprüft. Fehlt die Echo-Spielerliste nach einem Zug, bleibt eine bestätigte Zuordnung für dieselben Insassen gültig; ansonsten wird sie aus einem stabilen Paar von aktuellem Spieler und Zugseite ermittelt. Widersprüchliche Zwischenstände werden abgewartet, statt blind einen Zug abzusenden.

Die lokale Suche arbeitet mit iterativer Vertiefung, Alpha-Beta-Suche, Stellungsspeicher, Sofortgewinn-/Abwehrprüfung und Zentrum-/Reihenbewertung. Pro Berechnung gelten etwa 0,9 Sekunden, bis zu zwölf reguläre Suchebenen und 80.000 Suchknoten. Die Anzeige nennt die letzte vollständig abgeschlossene Tiefe; der Rest der Suche darf abgebrochen werden, ohne den letzten vollständigen Zug zu verlieren. „Gewinn/Remis nachgewiesen“ erscheint nur bei einer tatsächlich aufgelösten Suchstellung; sonst wird eine heuristische Einschätzung angezeigt. Anders als Tic Tac Toe wird Vier gewinnt damit nicht grundsätzlich bis zum Ende gelöst. Eine Sieg-Garantie gibt es nicht. Es werden keine Daten an einen Online-Dienst gesendet und keine zusätzliche EXE benötigt.

## Tic Tac Toe automatisch spielen

Unter **Scripts → Dieses Spiel → Tic Tac Toe** öffnen. Der Bereich erscheint nur im registrierten Spiel und Ort (Universe `7447878628`, Place `136162036182779`). Mit beiden Spielern am Tisch **Auto spielen** oder **Ein Zug** wählen; **Pause** beendet weitere automatische Züge. Jeder Start ist manuell, Autoplay bleibt nach beendeten Runden am selben Tisch aktiv und spielt nach dessen automatischem Reset weiter. Schach bleibt im selben Spielbereich erreichbar.

Das Brett wird direkt aus den replizierten Spieldaten gelesen. Die lokale vollständige Minimax-Suche berücksichtigt beide möglichen Startsymbole, sofortige Gewinne, Abwehr und Gabeln. Bei fehlerfreiem Gegenspiel endet eine ausgeglichene Partie remis; einen Sieg gegen jeden Gegner kann Tic Tac Toe nicht garantieren. Gewinnwege werden möglichst kurz, unvermeidbare Verluste möglichst spät gewählt. Es sind weder eine zusätzliche EXE noch ein Online-Dienst erforderlich.

Ein Zug wird nur für den eigenen Spieler am zugehörigen Tisch gesendet. Vor dem Senden wird die Stellung erneut geprüft; danach wird die vom Spiel gelieferte Belegung des Felds bestätigt. Es gibt keine blinden Wiederholungen. Aufstehen, Charakter- oder Tischwechsel stoppen die Automatik. Rundenende, Remis, automatische Brett-Resets und wechselnde Gegner am selben Sitz werden als Wartephase behandelt; neue Züge werden erst bei einer gültigen eigenen Spielzuordnung gesendet. Gewinnreihen werden in der Brettansicht durchgestrichen. Die Hauptkarte enthält Steuerung, Brett und die Einschätzung der letzten Berechnung.

## Piano automatisch spielen

1. Das Piano im Roblox-Spiel aktivieren bzw. dort hinsetzen.
2. Im ISB-Menü **Musik → Piano → Laden** öffnen und ein Lied suchen.
3. **Auswählen** lädt dieses Lied; **Spielen** startet die Tasteneingabe und schließt das Menü.
4. **F8** stoppt sofort und öffnet den Piano-Bereich. Pause und Tempo sind dort ebenfalls verfügbar.

Die Zeitleiste unter der Wiedergabe zeigt Minuten und Sekunden an. Ziehen pausiert kurz; beim Loslassen wird an der gewählten Stelle fortgesetzt, wenn das Lied vorher lief. Die Online-Liste bietet **Beliebt** (Downloadzahlen), **Neueste** (Katalog-ID) und **Titel A–Z**. Sterne merken Lieder; **Favoriten** filtert diese Liste und lässt sich mit Suche und Sortierung kombinieren. Favoriten und Sortierung werden mit den Einstellungen lokal gespeichert, sofern Dateizugriff verfügbar ist.

### Eigene MIDI- und VP-Textdateien

1. Eine `.mid`-/`.midi`-Datei herunterladen oder vorhandene VP-Player-Textdateien (`.txt` oder ohne Dateiendung) verwenden.
2. Im **Workspace-Ordner des Executors** den Unterordner **ISBMenu-MIDI** anlegen und die Datei hineinkopieren. „Ordner laden“ legt den Unterordner bei unterstützten Datei-APIs auch selbst an.
3. Im Menü **Musik → Piano → Eigene MIDIs → Ordner laden** wählen.
4. Das Lied **auswählen**, **vorhören** oder über **Spielen** am aktivierten Spiel-Piano abspielen.

Alternativ einen relativen Pfad wie `ISBMenu-MIDI/mein-lied.mid` oder `ISBMenu-MIDI/mein-lied.txt` eingeben und **Importieren** drücken. Für ältere VP-Dateien ohne Endung den Namen unverändert übernehmen. Dateien direkt im Workspace oder dessen anderen Unterordnern sind über ihren relativen Pfad ebenfalls möglich. Ein Pfad aus dem Windows-Downloads-Ordner funktioniert nicht automatisch: Der Executor begrenzt den Dateizugriff gewöhnlich auf seinen Workspace. Dies ist ein lokaler Dateiimport, kein Upload auf einen Server und kein Windows-Dateiauswahldialog.

Import prüft die Datei mit demselben MIDI-Parser; Ordnersuche liest zunächst nur die Namen und prüft die Datei beim Auswählen oder Vorhören. Unterstützt sind Standard-MIDI Format 0/1 bis 8 MB innerhalb der bestehenden Event-/Track-/Dauergrenzen. Audioformate wie MP3 und Musik-Webseitenlinks sind keine MIDI-Dateien. Eigene Lieder haben Suche, Favoriten, Titel-/Neueste-Sortierung, Vorschau, Tempo und Zeitleiste. Gespeichert werden die Bibliothekseinträge/Pfade und Favoriten; die Originaldateien müssen an ihrem Ort bleiben. Die Ordnersuche ist auf die erste Ebene von `ISBMenu-MIDI` begrenzt; Unterordner lassen sich über den Dateipfad importieren. Die Online-Liste bleibt separat. Fehlen Datei- oder Auflistungsfunktionen im Executor, zeigt das Menü einen Hinweis; mit `readfile` allein bleibt der Pfadimport möglich.

VP-Text wird als Notenschrift gelesen: einzelne Tasten, Akkorde wie `[tY]`, Pausen `|` und Kommentare mit `#`. Der `#META`-Kopf des VP-Players liefert `bpm`, `subdiv` sowie gegebenenfalls `timings` und `holds`. Diese Angaben steuern die gemeinsame Wiedergabe-/Vorschau-Zeitleiste, einschließlich Pausen am Liedende. Ohne Metadaten gelten 120 BPM, vier Schritte pro Schlag und die übliche 80-Prozent-Haltezeit; mit dem Tempo-Regler lässt sich die Wiedergabe anpassen. Aus reiner Tastennotenschrift lassen sich verlorene MIDI-Tempo-/Instrument-/Dynamikdaten nicht wiederherstellen. Drum-Sheets werden nicht als Piano-Noten interpretiert. UTF-8 mit/ohne BOM und UTF-16 mit BOM werden unterstützt. Auch Textdateien unterliegen der 8-MB-/Noten-/Dauergrenze und werden niemals als Programmcode ausgeführt.

Songinformationen, Wiedergabe, Tempo und Zeitleiste sind in einer Hauptkarte zusammengefasst. Die Höhe richtet sich nach dem Text; bei schmalen Ansichten wandern die Tempo-Tasten kompakt in eine zweite Zeile derselben Karte.

Das von Roblox gemeldete Layout steht kompakt bei der Zeitanzeige. Interne Roblox-Tastencodes verwenden feste QWERTY-Positionen; deshalb bleibt die MIDI-Tonzuordnung bei QWERTZ erhalten, ohne einen zusätzlichen Y/Z-Tausch einzubauen. Die Menüsprache beeinflusst diese Zuordnung nicht.

**Vorschau** spielt einen lokal aus MIDI erzeugten Piano-Ausschnitt von bis zu 20 Sekunden, ohne Piano-Tasten im Spiel zu drücken. Ein weiterer Klick stoppt die Vorschau; Laden lässt sich ebenfalls abbrechen. Die Vorschau startet nicht die Spiel-Wiedergabe und ändert die Songauswahl nicht. Dafür braucht die Skriptumgebung lokale Datei- und Audio-Asset-Unterstützung. Seit 2.6.66 werden aufgenommene Flügeltöne mit natürlichem Anschlag und Ausklang verwendet; die MIDI-Anschlagstärke steuert die Dynamik. Die Vorschau ist eine Piano-Interpretation des MIDI, keine Originalaufnahme des jeweiligen Songs. Die Klavierbank (rund 3,7 MB) wird beim ersten Anhören geladen und bei verfügbarem Dateizugriff lokal zwischengespeichert. Auch innerhalb einer Sitzung wird sie wiederverwendet. Ist sie nicht erreichbar und nicht im Cache, erscheint ein Vorschaufehler; es gibt keinen Rückfall auf den alten künstlichen Klang. Start einer normalen Wiedergabe, Stop, F8 und Beenden räumen die Vorschau auf.

Klavieraufnahmen: **Salamander Grand Piano (Yamaha C5) von Alexander Holm**, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/), bereitgestellt über [Tone.js Audio](https://github.com/Tonejs/audio/tree/efd8296360f9526e379bfbe5c1698ff54d6a1d34/salamander). Für ISB auf 21 Töne in kleinen Terzen von C2 bis C7 reduziert, nach Mono/22.050 Hz/16 Bit konvertiert, auf höchstens vier Sekunden pro Sample gekürzt und mit gemeinsamer Pegelanpassung sowie kurzem Schluss-Fade versehen. Zwischenliegende Tonhöhen werden interpoliert. Die Aufnahmen behalten ihre eigene Lizenz; Details stehen in [assets/PIANO-SAMPLES-LICENSE.txt](assets/PIANO-SAMPLES-LICENSE.txt).

Für die Standard-Roblox-Kamera wird während der Piano-Wiedergabe nur die Shift-Lock-Tastenbelegung vorübergehend geleert. Shift-Noten werden weiterhin gesendet. Pause, Stop, Fehler und Beenden stellen die vorherige Belegung wieder her; zwischenzeitliche Änderungen anderer Skripte bleiben erhalten. Eigene Kamera-Systeme ohne diese Belegung können abweichen. Falls die automatische Sperre dort nicht verfügbar ist, erscheint ein Hinweis auf die Roblox-Einstellungen.

Die Online-Liste stammt wie beim VP-Player von nanoMIDI. Die eigenständige Windows-App muss dafür nicht laufen. Verwendet wird die übliche chromatische 61-Tasten-Belegung (C2–C7); Pianos mit anderen Steuerungen sind nicht allgemein abgedeckt. Die verwendete Skriptumgebung muss Roblox-interne Tasteneingaben unterstützen; PC-weite Tastaturfunktionen werden nicht verwendet. Falls der interne Eingabeweg fehlt oder blockiert ist, erscheint ein Hinweis. Beim Wechsel in andere Fenster läuft das Lied weiter, solange Roblox den Player weiter ausführt. Chat, das Roblox-Menü, Aufstehen nach sitzendem Start und Respawn unterbrechen die Wiedergabe und geben gehaltene Tasten frei. Bei einer längeren Unterbrechung durch Roblox pausiert der Player, damit keine verspäteten Noten nachgeholt werden. F8 wird innerhalb von Roblox verarbeitet; zum Stoppen nach dem Raustabben zurück ins Spiel wechseln. MIDI und Oberfläche wurden geprüft; eine Live-Prüfung der Tasteneingabe im Roblox-Spiel steht noch aus.

## Anti-Void mit Pixel-Recovery

Anti-Void im Bewegungsbereich kehrt zur letzten gespeicherten Bodenposition zurueck. Dabei loest sich deine lokale Darstellung in Pixel auf; eine cyanfarbene Lichtspur und die Kamera begleiten den Rueckflug. Am Ziel erscheint dein Avatar wieder. Die Darstellung basiert auf den bereitgestellten FallRecovery-Skripten und benoetigt im Menue kein FallRecoveryEvent und kein Serverskript.

Der eigentliche Charakter wird sofort am sicheren Ziel stabilisiert, waehrend der sichtbare Effekt fliegt. Die Erkennung verwendet weiterhin die bisherige Anti-Void-Fallgrenze. Kamera, Sichtbarkeit und Humanoid-Zustaende werden bei Abschluss, Abschalten, Respawn, Beenden oder einem Fehler bereinigt. Fliegen, Freecam, Quick Actions und Wegpunkt-Teleports beenden eine laufende Recovery. Eine bereits aktive serverseitige InFallRecovery verhindert einen zweiten Start.

Anti-Void speichert nur stabil unterstützte Positionen: Mitte und acht Punkte ringsum müssen festen, annähernd ebenen Boden haben. Die Rückkehr liegt mindestens eine Sekunde vor dem letzten geprüften Punkt (bei kurzer Historie am ältesten sicheren Punkt), mit mindestens drei Studs geprüftem Kantenabstand. Vor der Rückkehr wird der Boden erneut geprüft. Der ursprüngliche Abstand des Charakterkerns zum Boden bleibt erhalten; der frühere Aufschlag von fünf Studs entfällt. Bewegliche Plattformen werden nicht als Rückkehrziel gespeichert. Nach Respawn und Teleports beginnt die Historie neu.

Die Animation ist lokal sichtbar. Menue-Sounds und reduzierte Effekte beruecksichtigen die vorhandenen Einstellungen. Bei reduzierten Bewegungen erfolgt weiterhin der direkte Ruecksprung ohne Kameraflug. Sound-Assets muessen im Spiel freigegeben sein. Spielseitige Todeszonen oder Teleport-Regeln koennen eine lokale Anti-Void-Rettung verhindern.

## Spielerinfo-Item am Ende des Inventars

Nach Start, Respawn und einem ersetzten Backpack wartet unser Item auf eine Ladepause von 1,25 Sekunden nach dem letzten neu hinzugekommenen Spiel-Tool. Es wird danach wieder hinten in den Backpack eingefuegt. Bereits bekannte Tools beim normalen Aus- und Ablegen starten diese Wartezeit nicht erneut. Das ausgeruestete Spielerinfo-Item wird nicht zwangsweise abgelegt; eine ausstehende Korrektur folgt nach dem Ablegen. Fremde Tools werden nicht umgehaengt. Die konkrete Darstellung haengt weiterhin vom Inventarsystem des jeweiligen Spiels ab.

## Admin-Serverwechsel und aktive Keybinds

Unter **Einstellungen > Erkennung** laesst sich **Bei Admin automatisch Server wechseln** einschalten. Die Option ist anfangs aus und wird lokal gespeichert. Sie verwendet die vorhandene Erkennung des Spielbesitzers, konfigurierter Staff-IDs und oeffentlicher Gruppenrollen; diese Rollen sind Hinweise, keine verifizierten Berechtigungen. Bereits anwesende und neu beitretende erkannte Admins zaehlen, die eigene Person wird ausgeschlossen.

Der Wechsel sucht automatisch in bis zu drei Seiten oeffentlicher Server nach einem freien Ziel ausserhalb der aktuellen Sitzung. Parallele Erkennungen loesen keinen doppelten Wechsel aus. Abschalten, Verlassen des Admins und Beenden des Menues verwerfen noch nicht gesendete Anfragen. Bei Fehlern wartet die Funktion mindestens 60 Sekunden. Sie garantiert keinen adminfreien Zielserver; das Menue muss nach einem Teleport erneut gestartet werden, sofern der Executor es nicht selbst neu laedt.

Links mittig steht eine kompakte Liste aktiver Funktionen mit den aktuellen Tasten fuer Fliegen, Noclip, Highlights/ESP, Laufgeschwindigkeit und Freecam. Sie gilt auch bei Aktivierung per Menue und bleibt beim Schliessen des Hauptfensters sichtbar. Sind alle diese Funktionen aus, verschwindet die Liste. Aktive Funktionen werden nicht gespeichert.

## Schach im Spiel

Unter **Scripts > Dieses Spiel > Schach** stehen **Auto spielen**, **Pause** und **Ein Zug** bereit. Bei englischer Menuesprache heisst der Pfad **Scripts > This Game > Chess**. Der Bereich erscheint nur im registrierten Spiel und Place; **Local / Lokal** bleibt der separate Lua-Dateilader. Setze dich zuerst an einen Schachtisch. Die Stellung, eigene Farbe und das Zugrecht kommen direkt aus den vorhandenen Spieldaten; Bildschirmaufnahme, Mauskalibrierung und eine zusaetzliche EXE werden nicht benoetigt.

Standardmaessig berechnet **Stockfish** die Zuege online ueber https://chess-api.com/v1. Gesendet wird nur die Brettstellung als FEN mit den Analyseparametern, keine Roblox-Spieler-ID. Angefragt wird Tiefe 18; die Anzeige zeigt die tatsaechlich vom Dienst erreichte Tiefe. Internet und eine HTTP-Funktion des Executors sind erforderlich. En-passant-Felder werden nur fuer die Online-Anfrage entfernt, weil der Dienst diese gueltigen Spielstellungen sonst ablehnt. Echte legale En-passant-Kandidaten werden zusaetzlich durch Stockfish-Analyse ihrer Folgestellungen mit dem regulaeren Zug verglichen. Originalstellung und lokale Legalitaetspruefung bleiben erhalten. Bei Fehlern oder Zeitueberschreitung stoppt die Automatik, ohne still auf eine schwaechere Engine umzuschalten. **Offline** waehlt ausdruecklich die bisherige begrenzte Lua-Suche (Tiefe 4, maximal 7000 Knoten und 0,8 Sekunden). Die Auswahl wird gespeichert. Eine Sieg-Garantie gibt es nicht.

Der Server prueft die Zuege weiterhin. Vor jedem Zug werden Stellung und Version erneut verglichen; nach dem Senden wartet das Menue auf die erwartete bestaetigte Stellung. Bei Aussteigen, Gegner-/Tischwechsel, Neustart, Fehler oder ausbleibender Bestaetigung stoppt die Automatik. Auto spielen ist beim Laden ausgeschaltet. Ein Engine-Wechsel pausiert die Automatik. **Humanize** ist standardmaessig aus. Die Von-/Bis-Felder stellen einen Bereich von 0 bis 60 Sekunden ein (Vorgabe: 1,2 bis 3,2 Sekunden). Schalter und Werte werden gespeichert. Eingeschaltet wartet jeder berechnete Zug zufaellig innerhalb dieses Bereichs. Aenderungen gelten fuer die naechste noch nicht begonnene Zugpause. Nach dieser Pause werden Sitzplatz, Charakter, Stellung und Version erneut geprueft; Pause und Beenden verwerfen den wartenden Zug.

Live geprueft: der Stockfish-Aufruf aus dem verbundenen Executor lieferte fuer die Startstellung einen lokal geprueften legalen Zug d2d4 mit Tiefe 16 in rund 0,32 Sekunden; dabei wurde kein Zug gesendet. Der neue Menueaufbau startete ohne gemeldete Fehler und zeigt beide Engine-Schalter. Bereits zuvor wurde ein eigener Zug an Tisch 4, b1c3, mit exakt passender Serverstellung und Versionswechsel 73 auf 74 bestaetigt. Ein kompletter Partie-Durchlauf mit Stockfish ist noch nicht verifiziert. Die bisherige ChessPilot-App wurde nicht veraendert.

## Starten

```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/main/ISBMenu-GitHub-Loader.lua?isb="..game:GetService("HttpService"):GenerateGUID(false)))()
-- by Larsiopuw
```

Dieser Main-Loader fragt bei jedem Start den aktuellen GitHub-Commit ab und lädt dessen Skript. Eindeutige Abrufadressen verhindern die Wiederverwendung alter Cache-Antworten. Es muss keine Versionsnummer ausgewählt oder später im Loader geändert werden. Bei einem GitHub-API-Limit wird die Main-Datei mit einer neuen Abrufadresse geladen.


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

## Änderungshistorie

Zusammengehörige Zwischenstände sind als abgeschlossene Funktionen zusammengefasst. Technische Versuche und Prüfergebnisse stehen separat im Prüfbericht.

### 2.6.83

- 777 Auto-Spin unter Scripts > Dieses Spiel: sicher zum Knopf teleportieren und direkt bei Freigabe automatisch drehen. Optional beim freigeschalteten Titel stoppen; AFK-Schutz läuft nur während Auto-Spin.

### 2.6.81

- Vier gewinnt Auto-Player unter Scripts > Dieses Spiel mit lokaler Zugberechnung, Brettansicht, Gewinnlinien und Suchtiefe. Automatisches Spielen über weitere Runden sowie Pause und einzelne Züge.

### 2.6.80

- Tic Tac Toe Auto-Player unter Scripts > Dieses Spiel mit vollständiger lokaler Zugberechnung, Brettansicht und Gewinnlinien. Autoplay spielt weitere Runden am selben Tisch automatisch weiter, bis du pausierst oder aufstehst.

### 2.6.78

- Anti-Void mit Pixel-Recovery, cyanfarbener Lichtspur und Rückflug-Kamera. Die Rückkehr verwendet einen früheren, rundum geprüften Bodenpunkt mit Kantenabstand und ohne zusätzlichen Höhenversatz.

### 2.6.76

- Schach Auto-Player unter Scripts > Dieses Spiel: Stockfish oder Offline-Suche, automatisches Spielen und einzelne Züge mit frei einstellbarer zufälliger Zugpause.
- Optionaler Serverwechsel bei erkannten Spiel-Admins unter Erkennung, standardmäßig aus. Links mittig zeigt eine kompakte Liste aktive Funktionen mit ihren Keybinds.
- Das Spielerinfo-Item wird nach dem Laden der Spiel-Items am Ende des Inventars einsortiert.

### 2.6.72

- Piano Auto-Player mit Online-Bibliothek, Suche, Sortierung und Favoriten sowie Import eigener MIDI- und VP-Textdateien.
- Wiedergabe mit Pause, Stop, Zeitleiste und direkt veränderbarem Tempo. Vorschauen verwenden echte Piano-Aufnahmen.
- Roblox-interne Eingaben unterstützen Hintergrundwiedergabe und Tastaturlayouts; während des Spielens werden Hotbar und die normale Shift-Lock-Belegung vorübergehend gesperrt.

### 2.6.61

- Outfit Stealer kopiert Körperbau, Kleidung, Accessoires und verfügbare Animationen eines Spielers für deine lokale Ansicht.
- Kamera, gehaltene Items und Effekte berücksichtigen den kopierten Körper. Eigenes Outfit, Respawn und Beenden stellen die ursprüngliche Darstellung wieder her.

### 2.6.53

- Fliegen mit vier Geschwindigkeitsstufen, eigenen Geschwindigkeiten und mehreren gespeicherten Flugstilen.
- Flugbewegungen wechseln fließend; normale Laufanimationen und eigene Schrittgeräusche pausieren während des Flugs.

### 2.6.49

- Das Dock passt seinen Abstand an sichtbare Inventar-Slots und den geöffneten Rucksack an.
- Die Sitzungsdauer wird in Stunden, Minuten und Sekunden angezeigt.

### 2.6.45

- Wegpunkte pro Spiel speichern, umbenennen und löschen.
- Gespeicherte Positionen per Teleport oder Freecam aufrufen; erreichbar neben Rejoin und Serverhop.

### 2.6.43

- Die Oberfläche verwendet automatisch Deutsch bei deutscher Roblox-Sprache, ansonsten Englisch. Navigation, Einstellungen, Spielerinfo und Änderungshistorie sind übersetzt.

### 2.6.38

- Spielerinfo-Item zum Auswählen eines Spielers mit Profilkarte, Verifizierung, Kontodaten, Gruppenrolle und verfügbaren öffentlichen Profildaten.
- Freundschaft, Namenshistorie, Outfits und vollständige Spielerdetails sind direkt erreichbar. Ablegen des Items schließt die Karte.

### 2.6.37

- Freecam mit eigener Bewegung, freiem Blick und Teleport zur Kameraposition.
- L beendet Freecam; N teleportiert und beendet sie. Blickrichtung und Zoom bleiben beim Wechsel zurück erhalten.

### 2.6.27

- Optionale Windows-Musikverbindung mit Wiedergabesteuerung und Auswahl verfügbarer Medienquellen.
- Der kopierbare Einrichtungsbefehl richtet den automatischen Start der Verbindung bei der Windows-Anmeldung ein.

### 2.6.22

- Skript-Hub mit ScriptBlox, RoScripts, Suche, Favoriten und lokaler Dateibibliothek. Fremde Skripte werden erst nach ausdrücklichem Ausführen gestartet.
- Öffentliche Serverliste mit Sortierung, Seitennavigation, Beitreten und kopierbarem Join-Skript.

### 2.6.17

- Einheitliche abgerundete Oberflächen mit Akzentfarben, animierten Bedienelementen und persönlicher Begrüßung.
- Dock, Statusanzeige und Benachrichtigungen passen sich der gewählten Menüposition an.

### 2.6.7

- Quick Actions für lokale Interaktionen wie Auf dem Kopf, Huckepack und Umarmen, mit Spielerauswahl und Stoppen.

### 2.6.0

- Freunde und erkannte Spiel-Admins erhalten eigene Farben und Kennzeichnungen in Spielerliste und Highlights.

### 2.4

- Rollskalen und direkte Zahleneingabe für Bewegungswerte, Sichtfeld, Helligkeit und Lautstärke.
- Tastenbelegungen lassen sich ändern und speichern; Regler unterstützen Dezimalkomma und Dezimalpunkt.

### 2.3

- ISB Menu mit Dock-Navigation, Profil, Bewegung, Spielern, Servern, Darstellung, Skripten, Musik und Einstellungen.
- Einstellungen, Tasten, Reglerwerte und Favoriten werden lokal gespeichert.

## Funktionen

| Bereich | Enthalten |
| --- | --- |
| Start | Spiel, Spieler/Freunde, Executor, Sitzungsdauer und Rolle |
| Bewegung | Weicher kamerabezogener Flug, Noclip, Mehrfachsprung, Speed/Jump/Flight/FOV, Reset, Respawn, Rejoin, Serverhop |
| Spieler | Suche, Avatare, Beobachten, Kamerarückkehr, lokale Positionsänderung |
| Server | Öffentliche Server, Sortierung, Cursor-Seiten, Beitreten, Join-Script kopieren |
| Darstellung | Highlights, Namen/Entfernung, Tageslicht, Schatten, FOV |
| Skripte | ScriptBlox/RoScripts, Entdecken, Suche, gespeicherte Skripte, Quelltextvorschau, Kopieren, ausdrückliches Ausführen, lokale Lua-Dateien |
| Musik | Piano Auto-Player, Online-/lokale Lieder, Vorschau, optionale Windows-Musikverbindung, Roblox-Audio |
| Einstellungen | Akzent, Klänge, Tasten, Performance, Erkennung, Protokoll |
| Profil | Konto-/Sitzungsdaten, Speicherstatus, Export, lokale Verwaltungswerkzeuge |

Flug: WASD, Space hoch, linke Strg runter; Touch mit Bewegungssteuerung und Höhentasten. Reset aktualisiert Spielwerte und sichtbare Regler. Freunde werden blau, öffentlich erkennbare Spiel-Admins rot markiert.

## Speicherung und Rollen

Einstellungen werden automatisch in ISBMenu-settings.json im Dateibereich des Executors gespeichert. Dafür sind readfile/writefile nötig; fehlender Dateizugriff erscheint im Profil. Skript-Favoriten speichern Metadaten, keinen fremden Quelltext. Aktive Bewegungsmodi werden beim Neustart nicht automatisch eingeschaltet.

OwnerNames enthält Larsiopuw; zusätzliche Menü-Admins stehen als numerische UserIds in CONFIG.AdminUserIds. Die Rolle steuert lokale Menüwerkzeuge und vergibt keine serverseitigen Spielrechte. Erkannte Gruppen-Admins sind davon getrennt.

## Prüfung und Grenzen

Der aktuelle Prüfbericht steht in ISB-Pruefbericht.txt. Automatisierte Modell- und Browserprüfungen sind von den dort beschriebenen Live-Prüfungen im verbundenen Roblox-Client getrennt. Bewegung, Voice, Assets und Teleports hängen vom Spiel und Executor ab.

ScriptBlox nutzt die öffentliche API: Beliebt nach Aufrufen, Neu nach Aktualisierung. RoScripts nutzt öffentliche Trending-/Neu-Seiten und Such-HTML. Kein API-Key. Bei der Anbieterprüfung zu v2.3 lieferte ScriptBlox HTTP 200; der direkte RoScripts-Abruf wurde hier mit HTTP 403 blockiert. Anbieterfehler werden angezeigt; Website-Änderungen können Anpassungen erfordern. Fremder Code läuft erst nach ausdrücklichem Klick.

Vorschaubilder benötigen Dateizugriff und getcustomasset/getsynasset; PNG/JPEG werden unterstützt. Andernfalls bleibt eine gestaltete Ersatzfläche. Audio benötigt passende Asset-Freigaben. Heroicons unter beiliegender MIT-Lizenz; Interface-Klänge selbst synthetisiert.

Der experimentelle lokale Voice-Modus bietet keinen nachgewiesenen Schutz vor serverseitigen Voice-Sperren. Gruppenrollen werden anhand öffentlicher Bezeichnungen eingeordnet; versteckte oder anders benannte Rollen können fehlen. CONFIG.StaffUserIds ergänzt die Erkennung.

Erweiterungen: ISBMenu.AddAction, ISBMenu.Notify und ISBMenu.Destroy.

Designreferenz: [Apple Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/). Anbieter: [ScriptBlox](https://docs.scriptblox.com/docs/scripts/fetch), [RoScripts Trending](https://roscripts.io/trending).

<!-- -- by Larsiopuw -->
