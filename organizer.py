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

def get_unique_filename(destination_folder, filename):
    name, extension = os.path.splitext(filename)
    new_filename = filename
    counter = 1

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name}({counter}){extension}"
        counter += 1

    return new_filename

def organize_file(file_path):
    if os.path.isdir(file_path):
        return

    file_name = os.path.basename(file_path)
    _, extension = os.path.splitext(file_name)

    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:

            destination_folder = os.path.join(SOURCE_FOLDER, folder)
            os.makedirs(destination_folder, exist_ok=True)

            unique_name = get_unique_filename(destination_folder, file_name)
            destination = os.path.join(destination_folder, unique_name)

            shutil.move(file_path, destination)

            print(f"✅ Moved: {file_name} → {folder}/{unique_name}")
            return


def organize_existing_files():
    print("Scanning existing files...")

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)
        organize_file(file_path)


if __name__ == "__main__":
    organize_existing_files()