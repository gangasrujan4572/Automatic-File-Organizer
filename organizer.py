import os
import shutil

SOURCE_FOLDER = os.path.join(os.getcwd(), "test")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".doc", ".docx", ".txt"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}


def organize_file(file_path):
    if os.path.isdir(file_path):
        return

    file_name = os.path.basename(file_path)
    _, extension = os.path.splitext(file_name)

    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:

            destination_folder = os.path.join(SOURCE_FOLDER, folder)
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(destination_folder, file_name)

            shutil.move(file_path, destination)

            print(f"✅ Moved: {file_name} → {folder}")
            return


def organize_existing_files():
    print("Scanning existing files...")

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)
        organize_file(file_path)


if __name__ == "__main__":
    organize_existing_files()