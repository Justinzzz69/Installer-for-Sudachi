
# Sudachi Installer

Ein Skript zur automatischen Installation von Sudachi, das die Software, Firmware und Schlüsseldateien herunterlädt, entpackt und konfiguriert.

## Installation

1. Lade die Dateien und führe das Skript `main.py` aus.
   
   ```python
   python main.py
   ```

2. Das Skript lädt und installiert:
   - Sudachi-Anwendung
   - Firmware-Dateien
   - Schlüsseldateien (prod.keys)

## Funktionen

- **Automatische Downloads**: Das Skript lädt alle benötigten Dateien herunter und zeigt Fortschrittsbalken an.
- **Entpacken und Konfigurieren**: Die heruntergeladenen Dateien werden in die entsprechenden Verzeichnisse entpackt.
- **Fehlerprotokollierung**: Bei Problemen wird eine Logdatei `sudachi_installer.log` erstellt.

## Fehlerprotokoll

Fehler werden nur bei Bedarf in `sudachi_installer.log` gespeichert.

## Danksagungen

Erstellt von **Tapetenputzer**  
[GitHub](https://github.com/Justinzzz69)
```