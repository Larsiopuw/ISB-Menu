# ISB Menu 2.6.98 · by Larsiopuw


## Aufstehen vor Teleports

Alle Ortswechsel des eigenen Charakters verwenden eine gemeinsame Sitzfreigabe: Halloween hin/zurück, 777 und automatische Rückkehr, Spieler-Teleports, Wegpunkte, Aufzug, Tischfinder samt Rückweg, Freecam-Teleport und der Start von Roleplay sowie Anti-Void. Kamera-Bewegungen und Outfit-Kopien bleiben eigenständige Funktionen.

Bei belegtem Sitz wird zunächst mit getrennten Space-Down/Up-Eingaben und Humanoid-Sprung aufgestanden. Beim Warten auf einen Gegner am Schachtisch reicht ein Impuls. Nur während einer laufenden eigenen Schachrunde (phase = Playing) werden mindestens zwei getrennte Impulse ausgeführt. Erst nach freiem SeatPart, ausgeschaltetem Sit-/Seated-Status, gelöster eigener SeatWeld-Verbindung und freigegebener zuvor erkannter Minispiel-Belegung darf der Charakter versetzt werden. Die Freigabe muss kurz stabil bleiben. Es werden keine serverseitigen SeatWelds lokal gelöscht. Bei fehlendem VirtualInputManager dient der Humanoid-Sprung als Rückfall; auch dann wird die tatsächliche Freigabe verlangt. Chat-Eingabefelder erhalten keine künstlichen Leerzeichen.

Nach maximal 4,5 Sekunden ohne Freigabe wird der Teleport abgebrochen. Stop, Respawn, ein anderer Charakter und das Entladen des Menüs brechen wartende Vorgänge ab. Der Tischfinder erfasst den Rückkehrpunkt nach dem Aufstehen; Rückwege nach Stop prüfen den Sitz erneut. Anti-Void bewegt den Charakter während der Sitzfreigabe nicht durch einen parallel laufenden Animations-Tick. Bereits stehende Charaktere teleportieren ohne zusätzlichen Sprung oder Wartezeit.

Nach einem bestätigten Schach-Sitzausstieg wird der noch laufende Kameraübergang über CameraRig.exit(true) des Spiels beendet. Anschließend übernimmt die eigene Custom-/Humanoid-Kamera mit der zuvor erfassten normalen Blickrichtung und Entfernung. Fehlt diese Ansicht nach einem Laden direkt am Tisch, wird eine moderate Ansicht hinter dem Charakter verwendet. Der normale Blick wird nur außerhalb von Sitzen, Scriptable-Kameras, Freecam, Beobachtung und Automatik-Kamerafahrten erfasst.

Halloween sichert CFrame, Focus, CameraType, CameraSubject und FieldOfView vor dem Hinteleport. Erst nach dem Rückteleport wird diese Ansicht freigegeben; auch bei einem fehlgeschlagenen Rückweg wird der Kamera-Callback aufgeräumt. Dadurch wird keine Zwischenansicht der Schach-Ausfahrt als Rückkehrkamera gespeichert.

Prüfstatus dieser Änderung: Luau-Kompilierung, vorhandene Menütests, gezielte Zustands-/Abbruchtests und native Adaptertests mit nachgebildeter Roblox-API. Ein echter Ingame-Test des Aufstehens ist noch offen. Der aktuelle Spielzustand wurde lesend geprüft; die Unterscheidung nutzt die vorhandene Schach-Phase im View-Snapshot.

## Animierter Hintergrund

Die vorhandenen dunklen UIGradient-Farbfolgen von Fenster, Dock, Statusleiste und kleinen schwebenden Fenstern werden durch eine langsame sinusförmige Verschiebung und leichte Drehung animiert. Farben, Farbpunkte, Deckkraft und Kartenflächen bleiben unverändert. Es gibt keine zusätzlichen Lichtstreifen, dunklen Balken oder Effekt-Ebenen und keinen zusätzlichen Spielwelt-Blur.

Unter Einstellungen > Allgemein ist „Animierter Hintergrund“ standardmäßig eingeschaltet. Ausschalten stellt die ursprüngliche Ausrichtung und Position wieder her. „Animationen reduzieren“ zeigt den ursprünglichen statischen Verlauf und verkürzt die bestehenden Menü-Übergänge. Beide Einstellungen werden gespeichert. Verdeckte Flächen werden nicht animiert; ein einzelner gemeinsamer Callback begrenzt die Verlaufsänderungen auf höchstens 30 Aktualisierungen pro Sekunde und gibt entfernte Flächen wieder frei.

Der ursprüngliche Quellstand vor dieser Designänderung liegt zusätzlich lokal unter work/liquid-glass-baseline.lua. Die Browser-Vorschau verwendet die vorhandenen CSS-Verläufe mit langsamer Hintergrundbewegung; sie ist eine Vorschau und kein Nachweis einer echten optischen Lichtbrechung in Roblox.

## Tischfinder für die Brettspiele

In jedem der drei Minispiel-Menüs befindet sich der Tischfinder. „Nächsten Platz finden“ wählt anhand der tatsächlichen Sitzentfernung einen freien Platz. Alternativ lassen sich ein wartender Gegner oder ein vollständig leerer Tisch filtern; die aufklappbare Liste zeigt Namen, Belegung und Entfernung und erlaubt den gezielten Beitritt.

ESP ist pro Minispiel separat schaltbar und wird gespeichert. Grün bedeutet leer, Gelb ein Spieler wartet, Rot beide Plätze besetzt und Blau der eigene Tisch. Markierungen und Beschriftungen aktualisieren sich alle 0,5 Sekunden und werden beim Abschalten beziehungsweise Entladen entfernt. Die ESP-Optionen starten ohne vorhandene Einstellung ausgeschaltet.

Vor dem Teleport wird die Belegung erneut gelesen. Automatisches Hinsetzen verwendet den nativen Sitz und wartet bis zu vier Sekunden auf die tatsächliche Sitzverbindung und den eigenen Account in den Spieldaten des Tisches. Erst dann wird „Du sitzt am Tisch“ angezeigt. Bei einer fehlenden Bestätigung wird zur vorherigen Position zurückgekehrt. Wiederholte Klicks starten keine parallelen Teleports; Autoplay wird durch einen Tischbeitritt nicht automatisch eingeschaltet.

Andere aktive Bewegungs-/Farmsteuerungen und die drei Autoplayer werden vor dem Wechsel beendet. Ausgelagerte Sitze im internen Bereich außerhalb der Map werden nicht als erreichbare freie Plätze angeboten. Die gesamte Funktion ist auf das registrierte Spiel begrenzt.

## Auto-Angeln

Unter **Scripts > Dieses Spiel > Auto-Angeln > Öffnen** gibt es Start/Stop, erkannte Angel, bestätigte Fänge, Credits und Fangfortschritt. Nur im registrierten Spiel sichtbar. Startet beim Laden ausgeschaltet. Am Teich wird eine vorhandene goldene Angel bevorzugt, sonst die Standardangel. Die vom Spiel gewährte Angel wird ausgerüstet, ein gültiger Punkt im Wasser für den nativen Wurf ermittelt und der normale Aktivierungsablauf einschließlich Cooldown verwendet.

Die Steuerung hält/löst ausschließlich den nativen Linksklick-Zustand des Angelsystems. Sie liest Fischposition, Geschwindigkeit und blauen Bereich aus der laufenden Spielrunde und steuert mit Bremsvorlauf; Positionen, Fortschritt und Belohnungen werden nicht gesetzt. Im Executor sind die fremden Input-Verbindungen nicht als aufrufbare Funktionen verfügbar; deshalb wird die verifizierte gemeinsame Eingabevariable verwendet. Die eigentliche Balkenphysik, Darstellung und Serverübertragung bleiben beim Spiel. Dies benötigt getconnections/getupvalue/getupvalues/setupvalue in der Client-Laufzeit und ist an den geprüften FishingController gebunden.

Bei jedem Wurf wird ein anderes gültiges Ziel im inneren Teichbereich gewählt; die Figur bleibt dabei an ihrer Position. Der lokale Cooldown der Angel wird vor der Aktivierung geprüft. CastFailed wird als abgelehnter Wurf mit Wiederholungspause angezeigt und nicht als Fang-Cooldown. Nach sechs Ablehnungen in Folge stoppt die Funktion mit dem Hinweis, sich am Teich umzustellen und neu zu starten.

Nach einer Server-Caught-Bestätigung werden Fänge/Credits gezählt und 8,15 Sekunden bis zum nächsten Wurf gewartet. Stop beendet die eigene laufende Angelrunde, löst die Eingabe und entfernt den eigenen Ereignis-Listener; Respawn, ein Sitzplatz und konkurrierende Bewegungsfunktionen werden berücksichtigt. Weggehen vom Teich wartet auf eine wieder verfügbare Angel. Keine PC-weiten Mausklicks. Der zentrale Menü-AFK-Schutz bleibt aktiv. Hintergrundbetrieb wurde mit tatsächlich unfokussiertem Roblox geprüft; ein vollständiger Test bei minimiertem Roblox und ein 20-Minuten-AFK-Dauertest sind davon getrennt.

## Zentraler AFK-Schutz

Der AFK-Schutz startet automatisch mit dem ISB-Menü, unabhängig von geöffnetem Tab, gestarteter Automatik, Respawn oder minimiertem Menü. Ein erster Roblox-interner Eingabeimpuls erfolgt beim Laden: ein balanciertes rechtes Maus-Down/Up über VirtualInputManager an einem festen Randpunkt; bei nicht verfügbarem Backend dient VirtualUser als Rückfall. Es wird keine Taste gehalten. Bei mindestens 60 Sekunden ohne Client-Eingabe folgt alle 60 Sekunden ein weiterer Impuls. Player.Idled dient als zusätzliche Absicherung; eine 15-Sekunden-Entprellung verhindert Mehrfachaufrufe. Eingabefehler werden angezeigt und nach 15 Sekunden erneut versucht. Es werden keine PC-weiten Tastendrücke und keine fremden Idled-Verbindungen deaktiviert.

777 Auto-Spin verwendet dieselbe zentrale Instanz und erzeugt keinen eigenen Idle-Listener mehr. Stoppen einzelner Funktionen lässt den zentralen Schutz bestehen. Entladen beendet die eigenen Input-/Heartbeat-/Idle-Verbindungen; erneutes Inject ersetzt die alte Instanz. Diagnose zeigt Backend-Status und gesendete Impulse. Ein erfolgreicher API-Aufruf ist vom vollständigen 20-Minuten-Dauertest zu unterscheiden.

## Halloween-Event

Unter **Scripts > Dieses Spiel > Halloween-Event > Öffnen** gibt es eine eigene Seite mit Start/Stop. Die Funktion ist auf Universe 7447878628 / Place 136162036182779 begrenzt und startet beim Laden nicht automatisch. Drei getrennte Optionen steuern automatisches Klingeln (voreingestellt an), Spawn-Benachrichtigungen unten rechts (an) und orange Haus-Highlights durch Wände (an). Alle drei Optionen werden beim Umschalten in ISBMenu-settings.json gespeichert und beim erneuten Laden wiederhergestellt, inklusive ausgeschalteter Werte. Ohne gespeicherte Auswahl sind alle drei an. Start/Stop bleibt davon getrennt und startet niemals automatisch. Mit ausgeschaltetem automatischem Klingeln sind auch nur Hinweise/ESP möglich.

Die Erkennung verwendet HalloweenHouseSpawnId und den originalen Doorbell-Prompt, auch für Häuser, die vor Start bereits vorhanden waren. Nach dem Ende der Hausanimation wird ein bodennaher, kollisionsfreier Standplatz gewählt. Vor der ersten Eingabe werden 0,35 Sekunden für die Positionsreplikation abgewartet. Es werden ausschließlich freie Standplätze im Haus hinter der Klingel innerhalb der Prompt-Reichweite gewählt. Eine genaue Kollisionsprüfung berücksichtigt die tatsächliche Form hohler Haus-Meshes; ist kein sicherer Platz verfügbar, wird nicht nach draußen ausgewichen. Die Kamera blickt während des Besuchs aus dem Hausinneren auf die Klingel. Eigene Charakterteile und die lokale Outfit-Kopie werden dabei nur für die eigene Kamera ausgeblendet und anschließend wiederhergestellt. Bei Rückkehr, Stop, Fehler oder Charakterwechsel wird die Kameraübernahme beendet und die vorherige Ansicht wiederhergestellt, sofern dieselbe Kamera noch existiert. Die Eingabe verwendet InputHoldBegin/InputHoldEnd wie die native Prompt-Oberfläche des Spiels; der bisherige Executor-Aufruf wird hierfür nicht mehr verwendet. Solange die Bestätigung fehlt, wird genau dieser Klingel-Prompt mit kurzen Abständen von 0,4 Sekunden nach jedem vollständigen Tastendruck erneut angesprochen. Fremde Spieler-/Item-Prompts erhalten keine Eingabe.

Der Besuch wartet bis zu zwölf Sekunden auf die passende Servermeldung über Candy Corns UND den entsprechenden Anstieg von Profile.SeasonalCurrency in derselben Saison. Erst diese Bestätigung erhöht Eingesammelt/Candys und sperrt die Spawn-ID. Die Menge wird aus der Serverantwort übernommen, nicht auf 18 festgelegt. Eine explizite Bereits-eingesammelt-Antwort sperrt das Haus ohne eine neue Belohnung zu zählen. Bestätigte IDs werden mit Server- und Accountbindung gespeichert (höchstens 64); Stop/Start und erneutes Inject heben diese Sperre nicht auf. Für außerhalb des Menüs abgeholte Häuser ohne öffentliche Serverantwort kann das Menü keinen Anspruch erfinden: ohne Bestätigung wird kein Erfolg angezeigt.

Fehler oder fehlende Gutschriften sperren das Haus nicht: bis zu drei Versuche mit Pause und jeweils sicherer Rückkehr. Danach lässt sich mit Start oder Stop/Start erneut versuchen. Ein schneller Neustart wartet das Ende der alten Aktion ab und startet dann genau eine neue Steuerung. Bei Start werden bestehende Häuser sofort gescannt. Während der Bestätigung bleibt der Charakter im Klingelbereich und wird bei Verdrängung außerhalb der Reichweite wieder dorthin gestellt. Eine vorübergehend blockierte Standplatzsuche verwirft keine noch eintreffende Belohnung. Stop, Fehler und Zeitüberschreitung räumen den Bestätigungslistener auf und kehren zurück; ein neuer Charakter wird nie zur alten Position versetzt. Haus-Highlights und die gespeicherten Schalter bleiben separat. 777 Auto-Spin pausiert während des Besuchs seine Bewegung.

## Spielinformationen je Spieler

Im registrierten Spiel erscheint in der Spieler-Detailansicht und im scrollbaren Bereich des Spielerinfo-Items eine kompakte Karte. Sie zeigt Credits, Reputation, Spielzeit in Minuten, Streak, gespendete/erhaltene Werte sowie Spielraenge. Der aufklappbare Bereich enthaelt Beschreibung, aktiven Titel, Aura, Farbverlauf, ausgeruestete Items/Emojis sowie Gamepasses, freigeschaltete Titel und Items. Zahlen erhalten Tausenderpunkte. Ausruestung und Sammlung erscheinen in getrennten Gruppen mit Anzahl und einzelnen Titel-/Item-Eintraegen. Gamepass-Namen und Bilder werden asynchron ueber Roblox MarketplaceService ermittelt und zwischengespeichert; maximal zwei Abfragen laufen gleichzeitig, fehlgeschlagene Abfragen haben eine Wiederholungspause. Noch nicht verfuegbare Namen zeigen einen Lade-/Fehlerstatus statt roher IDs. Fehlende oder noch nicht geladene Werte erscheinen als Gedankenstrich statt erfundener Nullwerte. Der Inspector-Scrollbereich folgt der tatsaechlichen Kartenhoehe inklusive 24 Pixel Unterkante und UI-Skalierung, auch nach Aufklappen oder Metadatenupdates. Die ausgewaehlten Profile aktualisieren sich sekundenweise ohne kompletten Neuaufbau der Ansicht. Ausserhalb von Universe 7447878628 / Place 136162036182779 wird dieser Bereich nicht erstellt und kein Spielprofil gelesen. Es werden nur die aufgefuehrten Profilfelder und Session.Ranks gelesen, keine vollstaendigen Echo-Zustaende.

## VIP-Aufzug mit lokalem E-Knopf

Im registrierten Spiel erstellt das Menue an beiden Aufzug-Knoepfen eigene lokale ProximityPrompts. Ein einzelner Druck auf E teleportiert direkt zum gegenueberliegenden Aufzug, ausgerichtet zur Tuer und mit Bodenpruefung fuer die jeweilige Charaktergroesse. Das Spiel-Teleportereignis wird dabei nicht ausgeloest. Die normalen Prompts behalten ihre Haltezeit; sie sind nur lokal deaktiviert, damit sie den Tastendruck nicht ebenfalls verarbeiten. Beim Entladen werden die eigenen Knoepfe entfernt und die urspruenglichen Enabled-Zustaende wiederhergestellt. Neue/gestreamte Knoepfe werden erfasst. Die Funktion ist automatisch aktiv und auf dieses Spiel begrenzt. Ist das Ziel noch nicht geladen oder kein tragfaehiger Boden gefunden, erfolgt kein Teleport. Eine halbe Sekunde lokale Entprellung verhindert Doppelaktivierung.

## 777 Auto-Spin

Unter **Scripts → Dieses Spiel → 777 Auto-Spin** öffnen. **Auto-Spin starten** sucht einen freien, bodennahen Standplatz und teleportiert dorthin. Die Eingabe spricht gezielt den nativen Spin-Prompt mit InputHoldBegin/InputHoldEnd an. Bei HoldDuration=0 wird der Druck im selben Aufruf vollständig losgelassen: keine künstlichen 0,14 Sekunden Tastendauer und keine 0,4 Sekunden Wiederholungspause. Solange der Knopf lokal frei und der Start unbestätigt ist, folgt ein neuer Tap in jedem Heartbeat-Frame. Die Enabled-Freigabe wird außerdem direkt im Signal-Callback beansprucht. Nach Serverbestätigung pausiert die Eingabe bis zur nächsten Freigabe. Dauerhafte ausbleibende Bestätigung stoppt nach zehn Sekunden; tatsächliche Halte-Prompts behalten ihre erforderliche Haltezeit. Stop/Fehler/Entladen räumen gehaltene Eingaben auf. Es gibt keine allgemeinen Q-Tastendrücke auf andere Prompts oder PC-Anwendungen. Eigene bestätigte Ergebnisse zählen, fremde Drehungen werden abgewartet. Ping, Bild-/Heartbeat-Takt und Serverreihenfolge entscheiden über den Vorrang; weder ein fester CPS-Wert noch ein Sieg gegen einen anderen Autoklicker wird garantiert. Keine Änderung von Ergebnissen oder Gewinnchancen.

**Bei freigeschaltetem Titel stoppen** ist standardmäßig an. Wer 777 bereits besitzt, wird deshalb beim Start weder teleportiert noch dreht er weiter. Für weitere Drehungen kann diese Option bewusst ausgeschaltet werden. Ein bestätigtes eigenes 777 oder der entsprechende Profilfortschritt beendet die Automatik bei aktiver Option. Drehungen und letztes eigenes Ergebnis stehen kompakt in der Hauptkarte. **777-Gewinne** zeigt zusätzlich den gespeicherten Gesamtzähler aus dem Spielprofil, auch aus früheren Sitzungen. Er aktualisiert sich bei geöffneter Karte automatisch; noch nicht geladene Profildaten erscheinen als Gedankenstrich.

Der AFK-Schutz wird zentral für das gesamte geladene ISB-Menü betrieben, auch während Halloween auf ein Haus wartet oder Auto-Spin gestoppt ist. Auto-Spin verwendet diese gemeinsame Instanz. Ein 20-Minuten-Dauertest ist gesondert zu bewerten.

Start beendet aktive Flug-/Freecam-/Quick-Action-/Piano-Steuerung, damit sich diese nicht mit der Platzierung überlagert. Solange Auto-Spin aktiv ist, bringt es den Charakter nach Weglaufen oder Wegschubsen automatisch auf einen sicheren Platz am Knopf zurück. Auch innerhalb der Prompt-Reichweite wird eine Abweichung von mehr als zwei Studs korrigiert. Stop beendet diese Rückkehr sofort. Die Funktion startet nicht automatisch nach Laden oder Respawn und wird nicht als aktiv gespeichert. Sie ist an dasselbe registrierte Spiel/Place wie die drei Brettspiele gebunden und steht nach Schach, Vier gewinnt und Tic Tac Toe.

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

### 2.6.90

- Spielinformationen in Spieler-Details und Spielerinfo-Item: Credits, Ränge, Reputation, Spielzeit und Spenden mit Tausenderpunkten. Aufklappbare Ausrüstung und Sammlung mit Gamepassnamen und einzelnen Titel-/Item-Einträgen; live aktualisiert und nur im unterstützten Spiel sichtbar.

### 2.6.89

- VIP-Aufzug mit eigenen lokalen E-Knöpfen: direkt hinein und zurück teleportieren, mit gerader Ausrichtung und bodennaher Ankunft. Automatisch aktiv im unterstützten Spiel.

### 2.6.86

- 777 Auto-Spin unter Scripts > Dieses Spiel: sicher zum Knopf teleportieren und direkt bei Freigabe automatisch drehen. Optional beim freigeschalteten Titel stoppen; AFK-Schutz läuft nur während Auto-Spin. Gesamtzahl der 777-Gewinne direkt in der Hauptkarte. Automatische Rückkehr zum Knopf während Auto-Spin.

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

Die Spielinformationen verwenden eine feste abgerundete Rahmenfläche statt einer beim Vergrößern verzögert gezeichneten Konturlinie. Der Rahmen bleibt beim Auf-/Zuklappen ohne Scrollbewegung sichtbar, sowohl im Spieler-Tab als auch im Spielerinfo-Item. Rahmen und Inhalt befinden sich in derselben Karte innerhalb der Scrollliste. Ausschließlich der native Scroll-Ausschnitt schneidet beide ab: die begrenzten Rahmenflächen reichen mit Reserve über dessen Rand hinaus und erzeugen keine eigene, versetzte Schnittkante.
