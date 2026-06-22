import os, zipfile
from pathlib import Path

def backup(folder):
    folder = Path(folder)
    zip_name = Path(f"{folder.name}.zip")

    with zipfile.ZipFile(zip_name, 'w') as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                file_path = Path(foldername) / filename
                backup_zip.write(file_path, compress_type=zipfile.ZIP_DEFLATED)

    print(f"Backup of {folder} completed. File: {zip_name}")

folder_to_backup = input("Enter the folder path to backup: ")

if not Path(folder_to_backup).exists():
    print(f"Folder does not exist: {folder_to_backup}")
elif not Path(folder_to_backup).is_dir():
    print(f"Path is not a directory: {folder_to_backup}")
else:
    backup(folder_to_backup)
