```markdown
# Sudachi Installer & Uninstaller

This project provides a unified installer and uninstaller for the **Sudachi** application, including additional support for detecting and removing related applications such as **Suyu** and **Yuzu**. The program downloads necessary files, installs Sudachi, and provides a cleanup option to uninstall the application along with any related directories.

## Features

- Downloads and installs **Sudachi** with all necessary components.
- Downloads firmware and keys required for the application.
- Supports uninstallation of **Sudachi**, **Suyu**, and **Yuzu** applications.
- Automatically detects and removes directories related to **Sudachi**, **Suyu**, and **Yuzu** from both the **Desktop** and **AppData** folders.
- Progress bars and status updates during installation.
- Clean, single-click uninstaller.
- Custom installer icon (`ico.ico`).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Justinzzz69/sudachi_installer_uninstaller.git
   ```

2. **Install dependencies**:
   Make sure you have the required Python packages installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the executable**:
   Run the `build.py` script to compile the project into a single executable:
   ```bash
   python build.py
   ```

   This will generate an executable called `sudachi_installer_uninstaller.exe` in the `dist` folder, along with the custom icon.

4. **Run the installer**:
   Execute the generated installer to begin installing **Sudachi**.

## Uninstallation

To uninstall **Sudachi**, **Suyu**, and **Yuzu**, simply run the same executable. The uninstaller will automatically detect and remove the applications from the following locations:
- **Desktop**
- **AppData/Roaming**

## Usage

### Installation

- After running the `sudachi_installer_uninstaller.exe`, the application will:
  1. Download the **Sudachi** installer from the specified URL.
  2. Create a `sudachi` folder on your Desktop.
  3. Extract the contents into the folder.
  4. Run **Sudachi.exe** and wait for it to finish before continuing.

### Uninstallation

- The uninstaller will:
  1. Locate and delete the **Sudachi**, **Suyu**, and **Yuzu** directories on the Desktop and in **AppData**.
  2. Provide a report of the deleted files and folders.

## Requirements

- **Python 3.7+** is required.
- Necessary Python libraries are listed in `requirements.txt`.
- You will need **PyInstaller** to build the executable.

## Icon

The installer uses a custom icon `ico.ico`. Ensure that the icon file is in the same directory as the `main.py` and `build.py` scripts during the build process.

## Platform

This project is **Windows-only**.

## Credits

Made by **Tapetenputzer**.

GitHub: [https://github.com/Justinzzz69](https://github.com/Justinzzz69)
```
