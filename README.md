# 🔐 System Security and Intrusion Detection Application

A Python-based desktop application designed to enhance system security by detecting unauthorized access attempts using authentication, security questions, and intrusion response mechanisms.

---

## 🚀 Features

* 🔑 Secure User Authentication (Username & Password)
* ❓ Randomized Security Questions (3 out of 10)
* 🚨 Intrusion Detection System
* 📩 Real-time Alerts using Pushover API
* ⚠️ Automatic System Shutdown after 3 failed login attempts
* 🖥️ GUI-based application using Tkinter
* ⌨️ Command-line version for testing and debugging

---

## 🛠️ Technologies Used

* Python
* MySQL
* Tkinter
* Requests Library

---

## 📁 Project Structure

```
System-Security-Intrusion-Detection/
│
├── main_ui.py        # GUI-based application
├── keylogger.py      # CLI-based version
├── database.sql      # Database setup file
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/anusharolla30-hash/system-security-intrusion-detection.git
cd system-security-intrusion-detection
```

---

### 2️⃣ Install Dependencies

```
pip install mysql-connector-python requests
```

---

### 3️⃣ Setup Database

Import the provided `database.sql` file into MySQL.

#### Option 1: Using MySQL Workbench

* Open MySQL Workbench
* Open `database.sql`
* Run the script

#### Option 2: Using Terminal

```
mysql -u root -p < database.sql
```

---

### 4️⃣ Run the Application

#### ▶️ GUI Version (Recommended)

```
python main_ui.py
```

#### ⌨️ CLI Version

```
python keylogger.py
```

---

## 🔐 How It Works

1. User enters login credentials
2. System verifies username and password
3. If correct → user answers 3 random security questions
4. If incorrect:

   * First wrong attempt → Alert notification sent
   * Three failed attempts → System shutdown

---

## ⚠️ Important Notes

* The application includes a system shutdown feature for security purposes
* Use correct credentials during testing to avoid unintended shutdown
* Update database credentials in code if needed

---

## 📌 Future Improvements

* Add real-time keystroke logging
* Integrate web-based dashboard (React + FastAPI)
* Implement password hashing (encryption)
* Add user activity monitoring

---

## 👨‍💻 Author

* Developed as a mini-project for System Security and Intrusion Detection

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
