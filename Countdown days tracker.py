import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import os

SAVE_FILE = "target_date.txt"

def save_target_date(date_str):
    with open(SAVE_FILE, "w") as f:
        f.write(date_str)

def load_target_date():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return f.read().strip()
    return None

def ask_for_date():
    date_str = simpledialog.askstring("Target Date", "Enter target date (YYYY-MM-DD):")
    if date_str is None:
        return target_date  # User cancelled
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        save_target_date(date_str)
        return date_str
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
        return ask_for_date()

def update_countdown():
    today = datetime.now().date()
    try:
        target = datetime.strptime(target_date[0], "%Y-%m-%d").date()
        days_left = (target - today).days
        if days_left >= 0:
            label.config(text=f"{days_left} day(s)\nremaining")
        else:
            label.config(text=f"Target date\npassed")
    except Exception as e:
        label.config(text="Invalid date")
    root.after(1000 * 60 * 60, update_countdown)  # update every hour

def close_app():
    root.destroy()

def open_menu(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()

def change_target_date():
    new_date = ask_for_date()
    if new_date:
        target_date[0] = new_date
        update_countdown()

# Tkinter UI setup
root = tk.Tk()
root.title("Countdown")
root.geometry("200x120")
root.configure(bg="yellow")
root.attributes("-topmost", True)
root.resizable(False, False)
root.overrideredirect(True)  # remove window frame

# Position window (top-right)
screen_width = root.winfo_screenwidth()
root.geometry(f"+{screen_width - 220}+50")

# Countdown label
label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="yellow", fg="black", justify="center")
label.pack(expand=True, fill='both')

# Close button
close_btn = tk.Button(root, text="X", command=close_app, bg="red", fg="white", bd=0, font=("Arial", 10, "bold"))
close_btn.place(x=175, y=0, width=25, height=25)

# Dropdown menu button (≡)
menu_btn = tk.Button(root, text="≡", bg="gray", fg="white", bd=0, font=("Arial", 10, "bold"))
menu_btn.place(x=150, y=0, width=25, height=25)
menu_btn.bind("<Button-1>", open_menu)

# Create popup menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Update Target Date", command=change_target_date)

# Load or set date (wrapped in list to make mutable in nested func)
target_date = [load_target_date()]
if not target_date[0]:
    target_date[0] = ask_for_date()

update_countdown()
root.mainloop()
