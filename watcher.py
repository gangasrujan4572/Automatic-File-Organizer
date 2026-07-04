import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import organizer


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        time.sleep(1)

        organizer.organize_file(event.src_path)


observer = None


def start_watching():

    global observer

    if observer is not None:
        return

    event_handler = FileHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        organizer.SOURCE_FOLDER,
        recursive=False
    )

    observer.start()

    print("Monitoring Started...")


def stop_watching():

    global observer

    if observer is not None:
        observer.stop()
        observer.join()
        observer = None

        print("Monitoring Stopped.")