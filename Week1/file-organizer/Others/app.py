import os
import shutil

# Folder to organize
source_folder = r"D:\AI SYSTEMS\Week1\file-organizer"

# File type categories
file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".pdf": "PDFs",
    ".txt": "Text",
    ".mp3": "Music",
    ".mp4": "Videos"
}

# Read all files
for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(file_name)

    # Find matching folder
    folder_name = file_types.get(extension.lower(), "Others")

    # Create folder if not exists
    folder_path = os.path.join(source_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Move file
    destination = os.path.join(folder_path, file_name)
    shutil.move(file_path, destination)

    print(f"Moved: {file_name} → {folder_name}")

print("Files organized successfully!")