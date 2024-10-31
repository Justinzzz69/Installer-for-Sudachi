import PyInstaller.__main__

# Liste der versteckten Importe
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

# Build main.py in eine ausführbare Datei
PyInstaller.__main__.run([
    'main.py',                 # Name des Hauptskripts
    '--name=SudachiInstaller', # Name der ausführbaren Datei
    '--onefile',               # Einzelne Datei erstellen
    '--icon=icon.ico',         # Optional: Icon-Datei hinzufügen
    *[f'--hidden-import={module}' for module in hidden_imports] # Versteckte Importe hinzufügen
])

print("Build abgeschlossen. Die ausführbare Datei befindet sich im Ordner 'dist'.")
