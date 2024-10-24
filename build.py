import os
import subprocess

# Define the name of the main script and output executable
main_script = "main.py"
output_exe = "sudachi_installer_uninstaller.exe"
icon_file = "ico.ico"  # Icon file for the executable

# Add all necessary hidden imports
hidden_imports = [
    "os",
    "shutil",
    "py7zr",
    "zipfile",
    "requests",
    "subprocess",
    "pathlib",
    "tqdm",
    "colorama"
]

# Build the PyInstaller command
hidden_imports_str = " ".join([f"--hidden-import={mod}" for mod in hidden_imports])
command = f"pyinstaller --onefile {hidden_imports_str} --name {output_exe} --icon={icon_file} {main_script}"

# Execute the command
try:
    subprocess.run(command, shell=True, check=True)
    print(f"{output_exe} has been successfully created with the icon!")
except subprocess.CalledProcessError as e:
    print(f"Error during compilation: {e}")
