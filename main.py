import os
import shutil
import py7zr
import zipfile
import requests
import subprocess
import time
from pathlib import Path
from tqdm import tqdm
import colorama
from colorama import Fore
import logging

# Initialize Colorama for colored output
colorama.init(autoreset=True)

# Error logging function, logs only if there is an error
def log_error(message):
    with open("sudachi_installer.log", "a") as log_file:
        log_file.write(f"{message}\n")

# Download a file with progress bar and retry mechanism
def download_file(url, save_path, retries=3, timeout=10):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, stream=True, timeout=timeout)
            response.raise_for_status()  # Raise error for bad status codes
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 KB

            with open(save_path, 'wb') as file, tqdm(
                    desc=f"Downloading {save_path.name}",
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
                    bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} ({rate_fmt})",
                    colour='cyan'
            ) as progress_bar:
                for chunk in response.iter_content(block_size):
                    file.write(chunk)
                    progress_bar.update(len(chunk))
            return True  # Successful download
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"{Fore.RED}Download attempt {attempt + 1} failed: {e}")
            attempt += 1
    return False  # Download failed after retries

# Directory setup function
def setup_directory(path):
    try:
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        return path.exists()
    except PermissionError as e:
        log_error(f"Permission error creating {path}: {e}")
        return False

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

    # Download Sudachi
    url_sudachi = "https://github.com/emuplace/sudachi.emuplace.app/releases/download/v1.0.11/sudachi-windows-v1.0.11.7z"
    if not download_file(url_sudachi, zip_path):
        print(f"{Fore.RED}Error: Failed to download Sudachi after several attempts.")
        return

    # Extract the downloaded 7z archive
    print(f"Extracting the downloaded file to {sudachi_folder_path}...")
    try:
        with py7zr.SevenZipFile(zip_path, 'r') as archive:
            archive.extractall(path=sudachi_folder_path)
        os.remove(zip_path)  # Delete the original 7z file
    except (py7zr.Bad7zFile, IOError) as e:
        log_error(f"Extraction error: {e}")
        print(f"{Fore.RED}Error extracting the file: {e}")
        return
    print("File successfully extracted!")

    # Automatically launch and close Sudachi
    sudachi_exe_path = sudachi_folder_path / "sudachi.exe"
    if sudachi_exe_path.exists():
        print(f"Launching Sudachi: {sudachi_exe_path}")
        try:
            process = subprocess.Popen([sudachi_exe_path])
            time.sleep(2)  # Wait before closing
            process.terminate()  # Close the process
            print(f"{Fore.GREEN}Sudachi launched and closed successfully.")
        except Exception as e:
            log_error(f"Error launching Sudachi: {e}")
            print(f"{Fore.RED}Error launching Sudachi: {e}")
            return
    else:
        log_error("sudachi.exe not found after extraction.")
        print(f"{Fore.RED}Error: sudachi.exe not found.")
        return

    # Firmware and keys download paths
    url_firmware = "https://github.com/THZoria/NX_Firmware/releases/download/19.0.0/Firmware.19.0.0.zip"
    url_keys = "https://files-prodkeys.b-cdn.net/prodkeys/Prodkeys.net_v19.0.0.zip"
    firmware_path = Path.home() / "AppData/Roaming/sudachi/nand/system/Contents/registered"
    keys_path = Path.home() / "AppData/Roaming/sudachi/keys"

    if not setup_directory(firmware_path) or not setup_directory(keys_path):
        return

    # Download and extract firmware
    firmware_zip = desktop_path / "firmware.zip"
    if not download_file(url_firmware, firmware_zip):
        print(f"{Fore.RED}Error: Failed to download firmware.")
        return
    print("Extracting firmware...")
    try:
        with zipfile.ZipFile(firmware_zip, 'r') as zip_ref:
            zip_ref.extractall(firmware_path)
        os.remove(firmware_zip)
    except (zipfile.BadZipFile, IOError) as e:
        log_error(f"Error extracting firmware: {e}")
        print(f"{Fore.RED}Error extracting firmware: {e}")
        return
    print("Firmware successfully downloaded and extracted!")

    # Download and extract keys
    keys_zip = desktop_path / "Prodkeys.net_v19.0.0.zip"
    if not download_file(url_keys, keys_zip):
        print(f"{Fore.RED}Error: Failed to download keys.")
        return
    print("Extracting keys...")
    try:
        with zipfile.ZipFile(keys_zip, 'r') as zip_ref:
            zip_ref.extractall(keys_path)
        os.remove(keys_zip)

        # Move prod.keys to main keys directory and cleanup
        extracted_key_folder = keys_path / "Prodkeys.net_v19.0.0"
        prod_key_file = extracted_key_folder / "prod.keys"

        if prod_key_file.exists():
            shutil.move(str(prod_key_file), str(keys_path))
            shutil.rmtree(extracted_key_folder)  # Clean up folder
            print("Keys successfully downloaded, extracted, and organized!")
        else:
            log_error("prod.keys file not found in extracted folder.")
            print(f"{Fore.RED}Error: prod.keys file not found.")
    except (zipfile.BadZipFile, IOError) as e:
        log_error(f"Error extracting keys: {e}")
        print(f"{Fore.RED}Error extracting keys: {e}")

    # Final credits message
    print(f"{Fore.CYAN}All files successfully downloaded and processed.\n")
    print(f"{Fore.GREEN}Installation complete!")
    print(f"\n{Fore.YELLOW}Made by Tapetenputzer")
    print(f"{Fore.YELLOW}Visit my GitHub: https://github.com/Justinzzz69")

# Start installation
if __name__ == "__main__":
    install_sudachi()
