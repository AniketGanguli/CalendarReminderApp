import tkinter as tk
from tkinter import messagebox
import json
import datetime
import calendar
import os

REMINDER_FILE = "reminders.json"

def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"one_time": {}, "recurring": {}}
    return {"one_time": {}, "recurring": {}}

def save_reminders():
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f, indent=2)

reminders = load_reminders()

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar & Reminder App")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)

        today = datetime.date.today()
        self.current_year = today.year
        self.current_month = today.month

        for i in range(7):
            self.root.columnconfigure(i, weight=1)
        for i in range(10):
            self.root.rowconfigure(i, weight=1)

        self.header = tk.Label(self.root, font=("Helvetica", 16))
        self.header.grid(row=0, column=1, columnspan=5, pady=10, sticky="nsew")

        self.prev_btn = tk.Button(self.root, text="<<", command=self.prev_month)
        self.prev_btn.grid(row=0, column=0, sticky="nsew")

        self.next_btn = tk.Button(self.root, text=">>", command=self.next_month)
        self.next_btn.grid(row=0, column=6, sticky="nsew")

        self.draw_calendar()
        self.check_reminders()

    def draw_calendar(self):
        today = datetime.date.today()
        self.header.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                if widget.grid_info()["row"] != 0:
                    widget.destroy()

        self.header.grid(row=0, column=1, columnspan=5, pady=10, sticky="nsew")
        self.prev_btn.grid(row=0, column=0, sticky="nsew")
        self.next_btn.grid(row=0, column=6, sticky="nsew")

        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            tk.Label(self.root, text=day, font=("Helvetica", 12)).grid(row=1, column=i, sticky="nsew")

        first_day = datetime.date(self.current_year, self.current_month, 1)
        start_day = (first_day.weekday() + 1) % 7
        num_days = calendar.monthrange(self.current_year, self.current_month)[1]

        row, col = 2, start_day
        for day in range(1, num_days + 1):
            date_str = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
            is_today = date_str == str(today)
            btn_color = "yellow" if is_today else "white"

            btn = tk.Button(self.root, text=str(day), bg=btn_color,
                            command=lambda d=day: self.set_reminder(d))
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

            col += 1
            if col > 6:
                col = 0
                row += 1

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.draw_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.draw_calendar()

    def set_reminder(self, day):
        global reminders
        date_str = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
        win = tk.Toplevel(self.root)
        win.title(f"Set Reminder - {date_str}")
        win.geometry("300x250")

        tk.Label(win, text="Reminder:").pack(pady=5)
        entry = tk.Entry(win, width=40)
        entry.pack(pady=5)

        tk.Label(win, text="Time (HH:MM):").pack(pady=5)
        time_entry = tk.Entry(win, width=10)
        time_entry.insert(0, "09:00")
        time_entry.pack(pady=5)

        tk.Label(win, text="Recurring (optional):").pack(pady=5)
        recur_var = tk.StringVar(value="none")
        recur_options = ["none", "daily", "weekly", "monthly"]
        tk.OptionMenu(win, recur_var, *recur_options).pack(pady=5)

        def save():
            global reminders
            msg = entry.get().strip()
            reminder_time = time_entry.get().strip()
            recur_type = recur_var.get()

            if not msg:
                return

            if recur_type == "none":
                reminders["one_time"][date_str] = {"time": reminder_time, "text": msg}
            else:
                rec = reminders.setdefault("recurring", {})
                if recur_type == "daily":
                    rec.setdefault("daily", []).append({"time": reminder_time, "text": msg})
                elif recur_type == "weekly":
                    weekday = datetime.date(self.current_year, self.current_month, day).strftime("%A")
                    rec.setdefault("weekly", {}).setdefault(weekday, []).append({"time": reminder_time, "text": msg})
                elif recur_type == "monthly":
                    rec.setdefault("monthly", {}).setdefault(str(day), []).append({"time": reminder_time, "text": msg})

            save_reminders()
            self.draw_calendar()
            win.destroy()

        tk.Button(win, text="Save", command=save).pack(pady=10)

    def check_reminders(self):
        now = datetime.datetime.now()
        today_str = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M")
        daily = reminders.get("recurring", {}).get("daily", [])
        weekly = reminders.get("recurring", {}).get("weekly", {}).get(now.strftime("%A"), [])
        monthly = reminders.get("recurring", {}).get("monthly", {}).get(str(now.day), [])
        one_time = reminders.get("one_time", {}).get(today_str)

        for rem in daily + weekly + monthly:
            if rem["time"] == current_time:
                messagebox.showinfo("Reminder", f"{rem['time']} - {rem['text']}")

        if one_time and one_time["time"] == current_time:
            messagebox.showinfo("Reminder", f"{one_time['time']} - {one_time['text']}")

        self.root.after(60000, self.check_reminders)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
