import mysql.connector
import random
import os
import requests
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Database Configuration
# -----------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '@project2005',
    'database': 'security'
} 

def db_conn():
    return mysql.connector.connect(**DB_CONFIG)

def fetch_one(query, params=None):
    with db_conn() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchone()

def fetch_all(query, params=None):
    with db_conn() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()

def send_pushover(msg):
    token = "a6j5zudnzsk6e2attxdzhpoz752pcs"
    user = "ukbfwgzftz79h3uki25zrjd49kpq4x"
    requests.post("https://api.pushover.net/1/messages.json",
                  data={"token": token, "user": user, "message": msg})

# -----------------------------
# GUI Application
# -----------------------------
class SecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Security System")
        self.attempts = 0
        self.user = None

        # Load Login Screen
        self.show_login_screen()

    def show_login_screen(self):
        self.clear()
        self.root.configure(bg="#CBE7FF")

        tk.Label(self.root, text="Login",
                 font=("Arial", 20, "bold"),
                 bg="#CBE7FF").pack(pady=20)

        tk.Label(self.root, text="Username:", bg="#CBE7FF").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#CBE7FF").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login",
                  bg="#7AA2E3", fg="white",
                  width=15, command=self.check_password).pack(pady=20)

    def check_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = fetch_one("SELECT * FROM users WHERE username=%s", (username,))
        if user and user['password'] == password:
            self.user = user
            self.show_security_screen()
        else:
            self.attempts += 1
            messagebox.showwarning("Error", f"Wrong Password! Attempt {self.attempts}")

            if self.attempts == 1:
                send_pushover("⚠ Wrong password attempt on your device!")

            if self.attempts >= 3:
                os.system("shutdown /s /t 1")

    def show_security_screen(self):
        self.clear()
        self.root.configure(bg="#E3D0FF")

        tk.Label(self.root, text="Security Questions",
                 font=("Arial", 20, "bold"),
                 bg="#E3D0FF").pack(pady=20)

        all_questions = fetch_all(
            "SELECT question, answer FROM security_questions WHERE user_id=%s",
            (self.user['id'],)
        )

        self.questions = random.sample(all_questions, 3)

        self.answer_entries = []
        for q in self.questions:
            tk.Label(self.root, text=q['question'], bg="#E3D0FF").pack(pady=5)
            entry = tk.Entry(self.root)
            entry.pack()
            self.answer_entries.append((q['answer'], entry))

        tk.Button(self.root, text="Submit",
                  bg="#A078C5", fg="white",
                  width=15, command=self.validate_answers).pack(pady=20)

    def validate_answers(self):
        for correct, entry in self.answer_entries:
            if entry.get().strip().lower() != correct.lower():
                messagebox.showerror("Error",
                                     "Wrong Answer! System will shutdown!")
                os.system("shutdown /s /t 1")
                return

        messagebox.showinfo("Success", "🎉 Access Granted!")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# -----------------------------
# Run GUI
# -----------------------------
root = tk.Tk()
root.geometry("400x500")
app = SecurityApp(root)
root.mainloop()



# python main_ui.py in terminal