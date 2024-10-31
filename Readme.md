Hier ist eine Vorlage für die `README.md` Datei:

```markdown
# Sudachi Installer

Ein Installationsskript für die Sudachi-Software, inklusive Firmware und Keys, das auf einfache Weise die Installation, das Setup und das Entfernen von Sudachi automatisiert.

## Features

- Automatischer Download und Entpacken der benötigten Dateien (Sudachi, Firmware, Keys).
- Fortschrittsanzeige während des Downloads.
- Automatisches Starten und Schließen der `sudachi.exe`.
- Saubere Organisation der Dateien und Ordner.
- Nur bei Fehlern wird eine Logdatei erstellt (`sudachi_installer.log`).

## Installation

1. **Klonen Sie das Repository**:
   ```bash
   git clone https://github.com/Justinzzz69/SudachiInstaller.git
   cd SudachiInstaller
   ```

2. **Benötigte Python-Pakete installieren**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ausführen des Installers**:
   ```bash
   python main.py
   ```

4. **Auswahl des Vorgangs**: Sie können zwischen **Installation** und **Deinstallation** wählen.

## Usage

### Installation
- Der Installer lädt die `sudachi.exe` herunter und entpackt sie auf dem Desktop im Ordner `sudachi`.
- Die Firmware und die Keys werden automatisch in den entsprechenden Ordnern unter `AppData/Roaming/sudachi` gespeichert.

### Deinstallation
- Die Deinstallation entfernt alle Dateien und Ordner von Sudachi aus `AppData` und dem Desktop.

## Anforderungen

- Python 3.7 oder höher
- Module: `os`, `shutil`, `py7zr`, `zipfile`, `requests`, `subprocess`, `pathlib`, `tqdm`, `colorama`

## Build einer Exe-Datei

Sie können das Skript mithilfe von PyInstaller in eine eigenständige `.exe`-Datei umwandeln:

1. Führen Sie das `build.py` Skript aus:
   ```bash
   python build.py
   ```

2. Die ausführbare Datei wird im Ordner `dist` gespeichert.

## Fehlersuche

Wenn ein Fehler auftritt, wird dieser in `sudachi_installer.log` protokolliert. Diese Datei wird nur erstellt, wenn ein Fehler während des Installationsprozesses auftritt.

## Credits

**Made by Tapetenputzer**  
GitHub: [Justinzzz69](https://github.com/Justinzzz69)
```
