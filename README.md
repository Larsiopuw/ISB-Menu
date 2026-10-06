# ISB Menu 2.2 · by Larsiopuw

Helle Porzellanflächen, kühles Metallgrau, warmer Orange-Akzent. Feste Navigation unten mittig, eigene Statusleiste oben rechts und animierte Panels. Inspiriert vom Imperialen Sicherheitsbüro.

![Designvorschau mit ausdrücklich gekennzeichneten Beispieldaten](ISB-Vorschau.png)

## Starten

```lua
loadstring(game:HttpGet("https://raw.githubusercontent.com/Larsiopuw/ISB-Menu/main/ISBMenu.lua"))()
-- by Larsiopuw
```

Öffentliches Repository, lesbarer Quellcode. Der Aufruf lädt den aktuellen Stand von main. Alternativ ISBMenu.lua vollständig ausführen. ISBMenu-Loader.lua lädt die lokale Datei; ISBMenu-GitHub-Loader.lua enthält zusätzliche Fehlerprüfung.

| Taste | Funktion |
| --- | --- |
| M | Hauptpanel öffnen / schließen |
| K | Festes Dock einfahren / ausfahren |
| T | Mittige Skript-Schnellsuche |
| Escape | Schnellsuche oder Tastenaufnahme abbrechen |

Einstellungen → Tasten: Anklicken und gewünschte Taste drücken. Doppelte Belegungen werden abgewiesen. Beim Schreiben in Textfelder greifen die Tastenkürzel nicht. Alte RightShift-Einstellungen werden auf M umgestellt. Der aktive Dock-Tab klappt sein Panel ein. Das Avatarbild rechts öffnet dein Profil. Fenster und Dock lassen sich nicht verschieben. Einstellungen → Allgemein → Beenden räumt auf; erneutes Ausführen ersetzt die vorherige Instanz.

## Änderungen in 2.2

- Helle ISB-Oberfläche, Orange-Akzent, einheitliche Favoriten-Icons, runde Dock-Buttons ohne konkurrierende Ecken.
- Separate Statusleiste oben rechts: Spielerzahl, gemessene FPS, Ping. Keine Metriken im Panel-Kopf.
- Animierte Rahmen innerhalb der Gruppen; Schließen und Hover-Ende verstecken alles. Neue Übergänge können ältere Animationen abbrechen.
- Reset stellt die Spielwerte für Speed, Jump und FOV wieder her und aktualisiert gespeicherte Werte sowie sichtbare Regler. Fluggeschwindigkeit zurück auf 45.
- Kamerabezogener Flug mit weicher Beschleunigung/Bremsung. WASD, Space hoch, linke Strg runter; Touch mit Bewegungssteuerung und Höhentasten. AutoRotate/PlatformStand werden wiederhergestellt und Restbewegung beendet.
- Freunde blau, öffentlich erkennbare Spiel-Admins rot. Gruppenrollen über GetRolesInGroupAsync mit Kompatibilitäts-Fallback.
- Performance: Partikel-/Trail-/Beam-/Post-Effekt-Pause, Schatten und FPS-Limits, sofern der Executor das Limit lesen und setzen kann. Vorherige Zustände werden wiederhergestellt.
- Eigener lokaler Voice-Controller ohne externe Menü-Abhängigkeit oder fremde Menübezeichnungen.
- Profil mit Owner/Admin/Member und optionale Server-Anbindung für gemeinsame Overhead-Anzeigen.

## Funktionen

| Bereich | Enthalten |
| --- | --- |
| Start | Spielname, Spieler/Freunde, Executor und Version, Sitzungsdauer, ISB-Rolle |
| Bewegung | Fliegen, Noclip, Mehrfachsprung, Speed, Jump, Flight, FOV, Reset, Respawn, Rejoin, Serverhop |
| Spieler | Suche, Avatare, Beobachten, Kamerarückkehr und lokale Positionsänderung |
| Server | Öffentliche Server, Sortierung, Cursor-Seiten, Ping/FPS soweit geliefert, Beitreten, Join-Script kopieren |
| Darstellung | Highlights, Namen/Entfernung, Tageslicht, Schatten, FOV |
| Skripte | ScriptBlox/RoScripts, Anbieterwechsel, Quelltextvorschau, Kopieren, ausdrückliches Ausführen und lokale Lua-Dateien |
| Musik | Roblox-Audio-IDs, Warteschlange, Lautstärke, Pause, Timer und Stoppuhr |
| Favoriten | Gespeicherte Aktionen über den Stern bei einer Funktion |
| Einstellungen | Akzent, Klänge, Tasten, Performance, Erkennung und Protokoll |
| Profil | Rolle, Netzwerkstatus, Overhead-Verwaltung für Owner/Admin |

## Overhead-Anzeigen in deinen eigenen Spielen

1. Öffne dein Spiel in Roblox Studio.
2. Lege **ISBPresence.server.lua als Script in ServerScriptService** ab, genau eine Instanz pro Spiel.
3. Kontrolliere OWNER_NAMES (Standard Larsiopuw). Zusätzliche Menü-Admins: numerische Roblox-UserIds in ADMIN_IDS.
4. Veröffentliche die Änderung und starte einen neuen Server. ISB-Clients verbinden sich automatisch.

Der Server löst den Owner-Namen in eine Roblox-UserId auf und vergibt Rollen anhand der tatsächlichen Spieleridentität. Öffentlich erkannte Gruppen-Admins erhalten dadurch keine Menü-Adminrechte.

Registrierte Clients melden sich alle 20 Sekunden; nach 65 Sekunden ohne Meldung entfernt der Server die Registrierung. Die Anzeige enthält Namen und Rolle. Anklicken fordert einen Teleport zum registrierten, lebenden Ziel an; der Server prüft Registrierung, Ziel und Charaktere. Nur Owner und konfigurierte Menü-Admins dürfen die gemeinsame Anzeige im Profil ein-/ausschalten. Member haben keinen entsprechenden Schalter. Anfragen werden begrenzt; Rollenangaben vom Client werden nicht angenommen.

In Spielen ohne diese Server-Anbindung gibt es keine gemeinsame ISB-Nutzererkennung. Ein Executor sieht die lokalen Oberflächen anderer Spieler nicht. Das Menü zeigt die Funktion dort als nicht verfügbar. Registrierung ist eine Anwesenheitsmeldung, kein kryptographischer Nachweis eines unveränderten Clients. Öffentlicher Client-Code kann verändert werden; verbindliche Berechtigungen liegen deshalb auf dem Server.

## Prüfung und Grenzen

205 Client-Assertions und 14 Server-Assertions bestehen in einer simulierten Roblox-API. Alle Lua-Dateien kompilieren mit Luau 0.741. Die HTML-Vorschau wurde im Browser bedient und visuell geprüft; sie zeigt Beispieldaten und führt keine Roblox-/Executor-Funktionen aus.

**Kein Live-Test in Roblox/Executor durchgeführt.** Die Server-Anbindung wurde nicht in deinen Spielen installiert. Bewegung, Voice, Assets und lokale Teleports hängen vom Spiel und Executor ab.

„Anti-VC Ban“ bezeichnet einen experimentellen lokalen Voice-Modus: Er verwaltet zugängliche Voice-Signalverbindungen, erneuert die Verbindung und stellt gespeicherte Verbindungszustände beim Ausschalten wieder her. **Kein nachgewiesener Schutz vor serverseitigen Voice-Sperren.** Fehlende APIs werden angezeigt.

Gruppenrollen werden anhand öffentlicher Namen wie Admin, Owner, Developer, Moderator oder Staff eingeordnet. Das ist eine Erkennungshilfe, kein vollständiger Nachweis von Berechtigungen. Versteckte oder anders benannte Rollen können fehlen; StaffUserIds ergänzen die Erkennung.

ScriptBlox nutzt die öffentliche Such-/Detail-API; RoScripts nutzt öffentliches HTML und dort angegebene Raw-URLs. Kein API-Key. Anbieteränderungen oder Ausfälle können Anpassungen erfordern. Fremder Code läuft erst nach ausdrücklichem Klick. Audio braucht passende Asset-Freigaben. Icons/Klänge benötigen Dateizugriff plus getcustomasset/getsynasset. Heroicons unter beiliegender MIT-Lizenz; Interface-Klänge selbst synthetisiert.

Erweiterungen über ISBMenu.AddAction und ISBMenu.Notify; ISBMenu.Destroy räumt auf.

Quellen: [ISB-Referenz](https://www.starwars.com/databank/imperial-security-bureau), [Roblox GroupService](https://create.roblox.com/docs/reference/engine/classes/GroupService), [Heroicons](https://github.com/tailwindlabs/heroicons).

<!-- -- by Larsiopuw -->
