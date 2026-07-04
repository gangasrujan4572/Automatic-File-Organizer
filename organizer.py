from email import message
import os
import shutil
import logging
import json

with open("config.json", "r") as file:
    config = json.load(file)

SOURCE_FOLDER = config["source_folder"]
ENABLE_LOGGING = config["enable_logging"]

print("Source Folder:", SOURCE_FOLDER)
print("Logging Enabled:", ENABLE_LOGGING)

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "organizer.log"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

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

            try:
                shutil.move(file_path, destination)
                message = f"Moved: {file_name} → {folder}/{unique_name}"

                print(f"✅ {message}")
                logging.info(message)
            except Exception as e:
                error = f"Error moving {file_name}: {e}"
                print(f"❌ {error}")
                logging.error(error)
            return


def organize_existing_files():
    print("Scanning existing files...")
    logging.info("========== File Organizer Started ==========")

    count = 0

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            organize_file(file_path)
            count += 1

    print(f"\n📊 Scan Complete!")
    print(f"📁 Files processed: {count}")

    logging.info(f"Scan completed. Files processed: {count}")
    logging.info("========== File Organizer Finished ==========\n")


if __name__ == "__main__":
    organize_existing_files()