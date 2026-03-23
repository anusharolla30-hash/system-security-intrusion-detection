import mysql.connector
import random
import os
import getpass
import requests

# -----------------------------
# Database Configuration
# -----------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',                 
    'password': '@project2005',  
    'database': 'security'
}

# -----------------------------
# Database Helper Functions
# -----------------------------
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
    user = "uq1akgamftovkpb1r37e34om5amtds"   
    data = {
        "token": token,
        "user": user, 
        "message": msg
    }
    requests.post("https://api.pushover.net/1/messages.json", data=data)


# -----------------------------
# Authentication Functions
# -----------------------------
def password_ok(username, password):
    user = fetch_one("SELECT * FROM users WHERE username=%s", (username,))
    if user and user['password'] == password:
        return user
    return None

def get_security_questions(user_id, num_questions=3):
    rows = fetch_all("SELECT question, answer FROM security_questions WHERE user_id=%s", (user_id,))
    random.shuffle(rows)   # shuffle all questions
    return rows[:num_questions]  # pick only first N after shuffle


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("🚀 Keylogger Security System Started")

    # ✅ Test connection first
    try:
        conn = db_conn()
        print("✅ Connected to MySQL successfully!")
        conn.close()
    except mysql.connector.Error as e:
        print("❌ Database connection failed:", e)
        return

    attempts = 0
    username = input("Enter username: ")

    while True:
        pwd = getpass.getpass("Enter password: ")

        user = password_ok(username, pwd)

        if user:
            print("✅ Password correct! Now answering security questions...")
            questions = get_security_questions(user['id'])

            correct = True
            for q in questions:
                ans = input(q['question'] + " ").strip().lower()
                if ans != q['answer'].lower():
                    print("❌ Wrong security answer! (System would shut down here)")
                    os.system("shutdown /s /t 1")
                    correct = False
                    break

            if correct:
                print("🎉 Access granted! Welcome,", username)
            break

        else:
            attempts += 1
            print("❌ Wrong password attempt", attempts)

            if attempts == 1:
              print("📩 Owner notified!")
              send_pushover("🚨 ALERT: Someone tried to log in with wrong password on your system!")

            if attempts >= 3:
                print("⚠️ 3 wrong attempts! (System would shut down here)")
                os.system("shutdown /s /t 1")
                break

# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main()






