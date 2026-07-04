import tkinter as tk
from tkinter import filedialog
import json
import os

# ---------------- CONFIG ---------------- #

CONFIG_FILE = "config.json"

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)
else:
    config = {
        "source_folder": "",
        "enable_logging": True
    }

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Automatic File Organizer")
root.geometry("650x350")
root.resizable(False, False)

# ---------------- FUNCTIONS ---------------- #

def browse_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

        config["source_folder"] = folder

        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)

        status.config(text="📁 Folder Selected", fg="blue")


def start_monitoring():
    status.config(text="🟢 Monitoring Started", fg="green")

    # Later we will start watcher.py here


def stop_monitoring():
    status.config(text="🔴 Monitoring Stopped", fg="red")

    # Later we will stop watcher.py here


# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="📂 Automatic File Organizer",
    font=("Segoe UI", 20, "bold")
)

title.pack(pady=20)

# ---------------- FOLDER ---------------- #

frame = tk.Frame(root)
frame.pack(pady=10, padx=20)

folder_entry = tk.Entry(
    frame,
    width=55,
    font=("Segoe UI", 10)
)

folder_entry.insert(0, config["source_folder"])
folder_entry.pack(side=tk.LEFT, padx=10)

browse_button = tk.Button(
    frame,
    text="Browse",
    command=browse_folder,
    width=12,
    font=("Segoe UI", 10)
)

browse_button.pack(side=tk.LEFT)

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(root)
button_frame.pack(pady=25)

start_button = tk.Button(
    button_frame,
    text="▶ Start Monitoring",
    command=start_monitoring,
    width=18,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(
    button_frame,
    text="⏹ Stop Monitoring",
    command=stop_monitoring,
    width=18,
    bg="#E53935",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

stop_button.pack(side=tk.LEFT)

# ---------------- LOGGING ---------------- #

logging_var = tk.BooleanVar(value=config["enable_logging"])

logging_check = tk.Checkbutton(
    root,
    text="Enable Logging",
    variable=logging_var,
    font=("Segoe UI", 10)
)

logging_check.pack()

# ---------------- SAVE SETTINGS ---------------- #

def save_settings():

    config["source_folder"] = folder_entry.get()
    config["enable_logging"] = logging_var.get()

    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

    status.config(text="✅ Settings Saved", fg="green")


save_button = tk.Button(
    root,
    text="💾 Save Settings",
    command=save_settings,
    width=18,
    font=("Segoe UI", 10)
)

save_button.pack(pady=15)

# ---------------- STATUS ---------------- #

status = tk.Label(
    root,
    text="⚪ Ready",
    font=("Segoe UI", 11, "bold"),
    fg="blue"
)

status.pack()

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="Version 1.5",
    font=("Segoe UI", 9),
    fg="gray"
)

footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()