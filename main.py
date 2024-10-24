import os
import shutil
import py7zr
import zipfile
import requests
import subprocess
from pathlib import Path
from tqdm import tqdm
import colorama
from colorama import Fore

# Initialize Colorama
colorama.init(autoreset=True)

# Utility to download a file with progress bar
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # Block size for progress bar

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

# Utility to create directories
def setup_directory(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path.exists()

# Main installation function
def install_sudachi():
    print(f"{Fore.CYAN}Starting the Sudachi installation...")

    desktop_path = Path.home() / "Desktop"
    sudachi_folder_path = desktop_path / "sudachi"
    zip_path = desktop_path / "sudachi-windows-v1.0.11.7z"

    # Create sudachi folder on the desktop
    if not setup_directory(sudachi_folder_path):
        print(f"{Fore.RED}Error: Could not create the folder {sudachi_folder_path}.")
        return

    # Download URL
    url_sudachi = "https://github.com/emuplace/sudachi.emuplace.app/releases/download/v1.0.11/sudachi-windows-v1.0.11.7z"
    print(f"Downloading Sudachi from {url_sudachi}...")
    download_file(url_sudachi, zip_path)

    # Extract the downloaded 7z archive to the sudachi folder
    print(f"Extracting the downloaded file to {sudachi_folder_path}...")
    with py7zr.SevenZipFile(zip_path, 'r') as archive:
        archive.extractall(path=sudachi_folder_path)
    os.remove(zip_path)  # Delete the original 7z file
    print("File successfully extracted!")

    sudachi_exe_path = sudachi_folder_path / "sudachi.exe"

    if sudachi_exe_path.exists():
        print(f"Launching Sudachi: {sudachi_exe_path}")
        process = subprocess.Popen([sudachi_exe_path])
        print(f"Please close Sudachi to continue the installation...")
        process.wait()
        print("Sudachi has been closed. Continuing...")
    else:
        print(f"{Fore.RED}Error: sudachi.exe not found.")
        return

    # Download and extract additional files (firmware and keys)
    url_firmware = "https://github.com/THZoria/NX_Firmware/releases/download/18.1.0/Firmware.18.1.0.zip"
    url_keys = "https://usc1.contabostorage.com/b14312a874cd4fb8812c5c8860564d3a:prodkeysnet/ProdKeys.net-v18.-1-0.zip"

    firmware_path = Path.home() / "AppData/Roaming/sudachi/nand/system/Contents/registered"
    keys_path = Path.home() / "AppData/Roaming/sudachi/keys"

    if not setup_directory(firmware_path):
        print(f"{Fore.RED}Error: Could not create the folder {firmware_path}.")
        return
    if not setup_directory(keys_path):
        print(f"{Fore.RED}Error: Could not create the folder {keys_path}.")
        return

    print("Downloading firmware...")
    firmware_zip = desktop_path / "firmware.zip"
    download_file(url_firmware, firmware_zip)
    print("Extracting firmware...")
    with zipfile.ZipFile(firmware_zip, 'r') as zip_ref:
        zip_ref.extractall(firmware_path)
    os.remove(firmware_zip)  # Delete the ZIP file after extraction
    print("Firmware successfully downloaded and extracted!")

    print("Downloading keys...")
    keys_zip = desktop_path / "ProdKeys.net-v18.-1-0.zip"
    download_file(url_keys, keys_zip)

    if keys_zip.exists():
        print("Extracting keys...")
        try:
            with zipfile.ZipFile(keys_zip, 'r') as zip_ref:
                zip_ref.extractall(keys_path)
            os.remove(keys_zip)  # Delete the ZIP file after extraction
            print("Keys successfully downloaded and extracted!")
        except zipfile.BadZipFile:
            print(f"{Fore.RED}Error: The ZIP file is corrupted.")
        except Exception as e:
            print(f"{Fore.RED}Error extracting keys: {e}")
    else:
        print(f"{Fore.RED}Error: Keys ZIP file not found.")

    print(f"{Fore.CYAN}All files successfully downloaded and processed.\n")

# Uninstaller function
def uninstall_sudachi():
    print(f"{Fore.CYAN}Starting the uninstallation...")

    desktop_path = Path.home() / "Desktop"
    sudachi_folder_path = desktop_path / "sudachi"
    appdata_paths = [
        Path.home() / "AppData/Roaming/sudachi",
        Path.home() / "AppData/Local/sudachi",
        Path.home() / "AppData/LocalLow/sudachi",
        Path.home() / "AppData/Roaming/suyu",
        Path.home() / "AppData/Local/suyu",
        Path.home() / "AppData/LocalLow/suyu",
        Path.home() / "AppData/Roaming/yuzu",
        Path.home() / "AppData/Local/yuzu",
        Path.home() / "AppData/LocalLow/yuzu",
    ]

    # Check and delete directories on the desktop
    if sudachi_folder_path.exists() and sudachi_folder_path.is_dir():
        print(f"Deleting folder: {sudachi_folder_path}")
        shutil.rmtree(sudachi_folder_path)

    # Check and delete directories in AppData
    for path in appdata_paths:
        if path.exists() and path.is_dir():
            print(f"Deleting folder: {path}")
            shutil.rmtree(path)

    print(f"{Fore.GREEN}Uninstallation complete!")

    # Footer with credit
    print(f"\nMade by Tapetenputzer")
    print(f"Visit my GitHub: https://github.com/Justinzzz69")
    input("Press Enter to exit...")

# Main entry point
if __name__ == "__main__":
    choice = input("Do you want to (I)nstall or (U)ninstall Sudachi? ").strip().lower()
    if choice == "i":
        install_sudachi()
    elif choice == "u":
        uninstall_sudachi()
    else:
        print("Invalid choice, exiting...")
