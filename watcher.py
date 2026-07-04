import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from organizer import organize_file, SOURCE_FOLDER


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        time.sleep(1)

        try:
            organize_file(event.src_path)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":

    print("📂 Automatic File Organizer is running...")
    print(f"👀 Watching: {SOURCE_FOLDER}")

    event_handler = FileHandler()

    observer = Observer()
    observer.schedule(event_handler, SOURCE_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()