import os
import tarfile
import zipfile
import requests
import subprocess
from pathlib import Path
from tqdm import tqdm
import colorama
from colorama import Fore

# Initialisiere Colorama
colorama.init(autoreset=True)


# Hilfsfunktion zum Herunterladen einer Datei mit Fortschrittsbalken
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # Größe der Blöcke für den Fortschrittsbalken

    with open(save_path, 'wb') as file, tqdm(
            desc=save_path.name,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} ({rate_fmt})",
            colour='green',
    ) as progress_bar:
        for chunk in response.iter_content(block_size):
            file.write(chunk)
            progress_bar.update(len(chunk))


# Funktion zum Einrichten von Verzeichnissen
def setup_directory(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path.exists()


# Hauptfunktion
def main():
    print(f"{Fore.CYAN}Starte das Suyu Installationsskript...")

    # Desktop-Pfad und Zielordner definieren
    desktop_path = Path.home() / "Desktop"
    suyu_path = desktop_path / "suyu"
    tar_path = desktop_path / "suyu.tar.xz"

    # URL zum Herunterladen der Datei
    url_suyu = "https://git.suyu.dev/suyu/suyu/releases/download/v0.0.3/Suyu-Windows_x86_64.tar.xz"
    print(f"{Fore.YELLOW}Herunterladen von Suyu von {url_suyu}...")
    download_file(url_suyu, tar_path)

    # Entpacken des heruntergeladenen Tar-Archivs direkt auf den Desktop
    print(f"{Fore.YELLOW}Entpacke die heruntergeladene Datei...")
    with tarfile.open(tar_path, 'r:xz') as tar_ref:
        extracted_folder_name = tar_ref.getnames()[0].split('/')[0]  # Erstes Verzeichnis im Archiv
        tar_ref.extractall(desktop_path)
    os.remove(tar_path)  # Ursprüngliche TAR.XZ-Datei löschen
    print(f"{Fore.GREEN}Datei erfolgreich entpackt!")

    # Prüfen, ob ein Ordner "suyu" bereits existiert, und ihn ggf. umbenennen
    extracted_folder_path = desktop_path / extracted_folder_name
    if extracted_folder_path.exists() and not suyu_path.exists():
        extracted_folder_path.rename(suyu_path)
        print(f"{Fore.GREEN}Entpackter Ordner umbenannt in: {suyu_path.name}")

    # Pfad zur suyu.exe-Datei
    suyu_exe_path = suyu_path / "suyu.exe"

    # suyu.exe ausführen und warten, bis es beendet wird
    if suyu_exe_path.exists():
        print(f"Starte Suyu: {suyu_exe_path}")
        process = subprocess.Popen([suyu_exe_path])
        print(f"Bitte schließen Sie Suyu, um mit der Installation fortzufahren...")
        process.wait()
        print(f"Suyu wurde geschlossen. Fortfahren...")
    else:
        print(f"{Fore.RED}Fehler: suyu.exe wurde nicht gefunden.")
        return  # Beende das Skript, wenn die exe nicht gefunden wurde.

    # Weitere Dateien herunterladen und entpacken
    url_firmware = "https://github.com/THZoria/NX_Firmware/releases/download/18.1.0/Firmware.18.1.0.zip"
    url_keys = "https://usc1.contabostorage.com/b14312a874cd4fb8812c5c8860564d3a:prodkeysnet/ProdKeys.net-v18.-1-0.zip"

    firmware_path = Path.home() / "AppData/Roaming/suyu/nand/system/Contents/registered"
    keys_path = Path.home() / "AppData/Roaming/suyu/keys"

    # Überprüfen, ob die Ordner existieren, und beende das Skript, wenn nicht
    if not setup_directory(firmware_path):
        print(f"{Fore.RED}Fehler: Der Ordner {firmware_path} konnte nicht erstellt werden.")
        return
    if not setup_directory(keys_path):
        print(f"{Fore.RED}Fehler: Der Ordner {keys_path} konnte nicht erstellt werden.")
        return

    # Firmware herunterladen und entpacken
    print(f"Herunterladen der Firmware...")
    firmware_zip = desktop_path / "firmware.zip"
    download_file(url_firmware, firmware_zip)
    print(f"Entpacken der Firmware...")
    with zipfile.ZipFile(firmware_zip, 'r') as zip_ref:
        zip_ref.extractall(firmware_path)
    os.remove(firmware_zip)  # ZIP-Datei nach dem Entpacken löschen
    print(f"Firmware erfolgreich heruntergeladen und entpackt!")

    # Keys herunterladen und entpacken
    print(f"Herunterladen der Keys...")
    keys_zip = desktop_path / "keys.zip"
    download_file(url_keys, keys_zip)
    print(f"Entpacken der Keys...")
    with zipfile.ZipFile(keys_zip, 'r') as zip_ref:
        zip_ref.extractall(keys_path)
    os.remove(keys_zip)  # ZIP-Datei nach dem Entpacken löschen
    print(f"Keys erfolgreich heruntergeladen und entpackt!")

    print(f"{Fore.CYAN}Alle Dateien erfolgreich heruntergeladen, entpackt und bearbeitet.")


# Skript ausführen
if __name__ == "__main__":
    main()
