

---

```markdown
# 📅 Calendar & Reminder App

A desktop calendar application built using Python and Tkinter that allows users to schedule **one-time and recurring reminders** with a graphical calendar interface.

---

## ✨ Features

- 📆 **Visual Monthly Calendar Interface**
- 🔔 **One-time and Recurring Reminders**
  - Daily, Weekly, Monthly
- 🕒 **Popup Notifications** for due reminders
- 💾 **Local Storage** of reminders in `reminders.json`
- 🧠 **Auto-check every minute** for matching reminders
- 🧱 **Persistent Data** — reminders saved between sessions

---

## 📂 File Structure

```

CalendarReminderApp/
├── main.py             # Main application logic
├── reminders.json      # Stores saved reminders
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # Project documentation

````

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** – for GUI
- **json** – for local reminder storage
- **datetime, calendar, os** – standard Python modules

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed  
  [Download Python](https://www.python.org/downloads/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AniketGanguli/CalendarReminderApp.git
   cd CalendarReminderApp
````

2. Run the application:

   ```bash
   python main.py
   ```

> 📝 Ensure the filename matches your main script if it's not `main.py`.

---

## 📋 How to Use

1. **Navigate Months** with `<<` and `>>` buttons.
2. **Click a date** to add a new reminder.
3. Enter:

   * Reminder text
   * Time (format: HH\:MM)
   * Recurrence: none / daily / weekly / monthly
4. Hit **Save**.
5. The app runs a background check every minute and pops up reminders when due.

---

## 📸 Screenshot

*(Insert a screenshot here if available)*

---

## ⚠️ Limitations

* 🖥️ **Desktop only**: No mobile or web support
* 🔕 **No sound**: Reminders are shown as popups, no sound alerts
* 🕐 **Time-sensitive to system clock**: If the app is closed or system is off, reminders will be missed
* 🔄 **No editing/removing reminders**: You can only add; not yet modify or delete reminders
* 📁 **Single-user only**: No user accounts or multi-user support
* 🔐 **No encryption**: Reminders are stored in plain JSON

---

## 🔮 Future Enhancements

* 🧹 **Edit/Delete Reminders** via interface
* 🔔 **Add audio notifications**
* 📅 **Weekly/Daily calendar views**
* 🌐 **Cloud backup/sync**
* 📱 **Mobile (Android/iOS) versions**
* 🔒 **Password-protected reminders or app access**
* 🔁 **Advanced recurring patterns** (e.g., every 3 days, bi-weekly)
* 🧪 **Unit testing & CI pipeline** for production readiness



## 👤 Author

**Aniket Ganguli**
GitHub: [@AniketGanguli](https://github.com/AniketGanguli)

---

> Contributions, bug reports, and suggestions are welcome! Feel free to fork or submit pull requests.

```

