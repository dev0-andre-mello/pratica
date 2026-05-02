import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from datetime import datetime
import threading

config = {
    "source": "",
    "destination": "",
}

def load_config():
    if os.path.exists("backup_config.txt"):
        with open("backup_config.txt") as f:
            lines = f.read().splitlines()
            if len(lines) >= 2:
                config["source"] = lines[0]
                config["destination"] = lines[1]

def save_config():
    with open("backup_config.txt", "w") as f:
        f.write(config["source"] + "\n")
        f.write(config["destination"] + "\n")

def do_backup():
    src = config["source"]
    dst = config["destination"]

    if not src or not dst:
        messagebox.showwarning("Missing paths", "Set source and destination folders first.")
        return

    if not os.path.exists(src):
        messagebox.showerror("Error", f"Source folder not found:\n{src}")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"silksong_backup_{timestamp}"
    backup_path = os.path.join(dst, backup_name)

    def run():
        btn_backup.config(state="disabled", text="Backing up...")
        lbl_status.config(text="⏳  Copying files...", fg=COLOR_YELLOW)
        root.update()
        try:
            shutil.copytree(src, backup_path)
            lbl_status.config(text=f"✔  Backup saved: {backup_name}", fg=COLOR_GREEN)
            refresh_backup_list()
        except Exception as e:
            lbl_status.config(text=f"✘  Error: {e}", fg=COLOR_RED)
        finally:
            btn_backup.config(state="normal", text="⚔  BACKUP SAVE")

    threading.Thread(target=run, daemon=True).start()

def restore_backup():
    selection = listbox.curselection()
    if not selection:
        messagebox.showinfo("Restore", "Select a backup from the list first.")
        return

    backup_name = listbox.get(selection[0])
    backup_path = os.path.join(config["destination"], backup_name)
    src = config["source"]

    if not os.path.exists(backup_path):
        messagebox.showerror("Error", "Backup folder not found.")
        return

    confirm = messagebox.askyesno(
        "Restore backup",
        f"This will REPLACE your current save with:\n\n{backup_name}\n\nContinue?"
    )
    if not confirm:
        return

    try:
        if os.path.exists(src):
            shutil.rmtree(src)
        shutil.copytree(backup_path, src)
        lbl_status.config(text=f"✔  Restored: {backup_name}", fg=COLOR_GREEN)
    except Exception as e:
        lbl_status.config(text=f"✘  Restore error: {e}", fg=COLOR_RED)

def delete_backup():
    selection = listbox.curselection()
    if not selection:
        return
    backup_name = listbox.get(selection[0])
    backup_path = os.path.join(config["destination"], backup_name)
    confirm = messagebox.askyesno("Delete", f"Delete backup:\n{backup_name}?")
    if confirm:
        shutil.rmtree(backup_path)
        refresh_backup_list()
        lbl_status.config(text=f"🗑  Deleted: {backup_name}", fg=COLOR_YELLOW)

def refresh_backup_list():
    listbox.delete(0, tk.END)
    dst = config["destination"]
    if os.path.exists(dst):
        backups = sorted(
            [d for d in os.listdir(dst) if d.startswith("silksong_backup_")],
            reverse=True
        )
        for b in backups:
            listbox.insert(tk.END, b)
        lbl_count.config(text=f"{len(backups)} backup(s)")
    else:
        lbl_count.config(text="0 backups")

def pick_source():
    path = filedialog.askdirectory(title="Select save folder (source)")
    if path:
        config["source"] = path
        lbl_src.config(text=path)
        save_config()

def pick_destination():
    path = filedialog.askdirectory(title="Select backup folder (destination)")
    if path:
        config["destination"] = path
        lbl_dst.config(text=path)
        save_config()
        refresh_backup_list()

# -> UI
BG          = "#0e0e12"
BG2         = "#16161e"
BG3         = "#1e1e2a"
COLOR_SILK  = "#c8a96e"   # gold/silk tone
COLOR_STEEL = "#8ab4d4"   # steel heart blue
COLOR_GREEN = "#6fcf97"
COLOR_RED   = "#eb5757"
COLOR_YELLOW= "#f2c94c"
TEXT        = "#e8e0d0"
TEXT_DIM    = "#6b6670"

root = tk.Tk()
root.title("Silksong — Steel Heart Backup")
root.geometry("620x540")
root.resizable(False, False)
root.configure(bg=BG)

load_config()

# Header
header = tk.Frame(root, bg=BG, pady=16)
header.pack(fill="x", padx=24)

tk.Label(header, text="⚔", font=("Segoe UI Emoji", 28), bg=BG, fg=COLOR_SILK).pack(side="left", padx=(0, 10))
title_frame = tk.Frame(header, bg=BG)
title_frame.pack(side="left")
tk.Label(title_frame, text="STEEL HEART BACKUP", font=("Courier New", 16, "bold"),
         bg=BG, fg=COLOR_SILK).pack(anchor="w")
tk.Label(title_frame, text="Hollow Knight: Silksong — Save Manager",
         font=("Courier New", 8), bg=BG, fg=TEXT_DIM).pack(anchor="w")

# Divider
tk.Frame(root, bg=COLOR_SILK, height=1).pack(fill="x", padx=24)

# Paths
paths_frame = tk.Frame(root, bg=BG2, pady=14, padx=20)
paths_frame.pack(fill="x", padx=24, pady=(14, 0))

def path_row(parent, label_text, current_val, command):
    row = tk.Frame(parent, bg=BG2)
    row.pack(fill="x", pady=4)
    tk.Label(row, text=label_text, font=("Courier New", 8, "bold"),
             bg=BG2, fg=TEXT_DIM, width=14, anchor="w").pack(side="left")
    lbl = tk.Label(row, text=current_val or "Not set", font=("Courier New", 8),
                   bg=BG3, fg=TEXT, anchor="w", padx=8,
                   relief="flat", width=44, cursor="hand2")
    lbl.pack(side="left", padx=(0, 8))
    tk.Button(row, text="Browse", font=("Courier New", 8), bg=BG3, fg=COLOR_STEEL,
              relief="flat", padx=8, cursor="hand2", command=command,
              activebackground=COLOR_STEEL, activeforeground=BG).pack(side="left")
    return lbl

lbl_src = path_row(paths_frame, "SAVE FOLDER", config["source"], pick_source)
lbl_dst = path_row(paths_frame, "BACKUP FOLDER", config["destination"], pick_destination)

# Backup button
btn_frame = tk.Frame(root, bg=BG, pady=16)
btn_frame.pack()

btn_backup = tk.Button(
    btn_frame, text="⚔  BACKUP SAVE",
    font=("Courier New", 14, "bold"),
    bg=COLOR_SILK, fg=BG,
    relief="flat", padx=32, pady=12,
    cursor="hand2",
    activebackground="#e0c07a", activeforeground=BG,
    command=do_backup
)
btn_backup.pack()

# Status
lbl_status = tk.Label(root, text="Ready — no backup made yet.",
                      font=("Courier New", 8), bg=BG, fg=TEXT_DIM)
lbl_status.pack()

# Backup list
tk.Frame(root, bg=COLOR_STEEL, height=1).pack(fill="x", padx=24, pady=(12, 0))

list_header = tk.Frame(root, bg=BG, pady=6)
list_header.pack(fill="x", padx=24)
tk.Label(list_header, text="BACKUPS", font=("Courier New", 9, "bold"),
         bg=BG, fg=COLOR_STEEL).pack(side="left")
lbl_count = tk.Label(list_header, text="0 backups", font=("Courier New", 8),
                     bg=BG, fg=TEXT_DIM)
lbl_count.pack(side="right")

list_frame = tk.Frame(root, bg=BG, padx=24)
list_frame.pack(fill="both", expand=True, pady=(0, 4))

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                     font=("Courier New", 8), bg=BG3, fg=TEXT,
                     selectbackground=COLOR_STEEL, selectforeground=BG,
                     relief="flat", borderwidth=0, activestyle="none", height=7)
listbox.pack(fill="both", expand=True)
scrollbar.config(command=listbox.yview)

# Action buttons
action_frame = tk.Frame(root, bg=BG, pady=8)
action_frame.pack(fill="x", padx=24)

tk.Button(action_frame, text="↩  Restore selected",
          font=("Courier New", 9), bg=BG3, fg=COLOR_GREEN,
          relief="flat", padx=16, pady=6, cursor="hand2",
          activebackground=COLOR_GREEN, activeforeground=BG,
          command=restore_backup).pack(side="left", padx=(0, 8))

tk.Button(action_frame, text="🗑  Delete selected",
          font=("Courier New", 9), bg=BG3, fg=COLOR_RED,
          relief="flat", padx=16, pady=6, cursor="hand2",
          activebackground=COLOR_RED, activeforeground=BG,
          command=delete_backup).pack(side="left")

# Init
refresh_backup_list()
root.mainloop()
