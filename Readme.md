```markdown
# Sudachi Installer

Dies ist ein einfaches Installationsskript für Sudachi, das die erforderlichen Dateien und Firmware automatisch herunterlädt und installiert. Es erleichtert die Installation und Einrichtung von Sudachi auf deinem Computer.

## Anforderungen

- Python 3.6 oder höher
- Die folgenden Python-Pakete:
  - `requests`
  - `py7zr`
  - `zipfile`
  - `tqdm`
  - `colorama`

Diese Pakete können mit dem folgenden Befehl installiert werden:

```bash
pip install requests py7zr tqdm colorama
```

## Verwendung

1. Klone das Repository oder lade die Dateien herunter.
2. Führe das Skript `main.py` aus:

   ```bash
   python main.py
   

3. Das Skript wird automatisch die folgenden Schritte durchführen:
   - Download von Sudachi
   - Extraktion der Sudachi-Dateien
   - Download und Extraktion der Firmware
   - Download und Organisation der Schlüsseldateien (`prod.keys`)

4. Am Ende wird Sudachi automatisch gestartet und anschließend geschlossen.

## Fehlerprotokollierung

Wenn während des Installationsprozesses Fehler auftreten, werden diese in der Datei `sudachi_installer.log` protokolliert. Überprüfe diese Datei, um detaillierte Informationen über etwaige Probleme zu erhalten.

## Hinweis

- Stelle sicher, dass du über die erforderlichen Berechtigungen verfügst, um die Ordner zu erstellen und Dateien herunterzuladen.
- Das Skript erstellt einen Ordner namens `sudachi` auf deinem Desktop und installiert alle erforderlichen Dateien dort.

## Danksagungen

Dieses Skript wurde von **Tapetenputzer** erstellt. Für weitere Informationen und den Quellcode, besuche bitte das [GitHub-Repository](https://github.com/Justinzzz69).
```
