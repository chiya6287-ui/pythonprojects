import json
import time
import logging
import sqlite3
import requests
from datetime import datetime

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive

    def show_greeting(self):
        return f"{self.greet} & {self.receive}"

class Condition:
    def __init__(self):
        self.attempts = 0

    def head_condition(self):
        while True:
            try:
                feel = input("\nEnter what you are feeling (mental stress, mental pressure, headache)?\n")

                if feel.isdigit():
                    raise ValueError("Digits are not allowed")
                elif feel in ["mental stress", "mental pressure", "headache"]:
                    verdict = ("serious for brain", "check brain specialist")
                    logging.info(f"Condition matched: {verdict}")
                    return verdict
                else:
                    print("Not match, please choose right")
                    self.attempts += 1
            except ValueError as e:
                print(e)
                logging.warning("Invalid input detected")
                self.attempts += 1

            if self.attempts >= 2:
                print("Please wait for 10 seconds before trying again...")
                time.sleep(10)
                self.attempts = 0

class DataManager:
    def __init__(self, db_name="user_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS conditions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                condition TEXT,
                advice TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def save_to_db(self, condition, advice):
        self.cursor.execute("INSERT INTO conditions (condition, advice, timestamp) VALUES (?, ?, ?)",
                            (condition, advice, datetime.now().isoformat()))
        self.conn.commit()

    def close(self):
        self.conn.close()

def fetch_health_tip():
    """Simulate API call for health tips"""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()["title"]
    except Exception as e:
        logging.error(f"API error: {e}")
        return "Stay hydrated and take rest."

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("\n", datetime.now())

    greet = Greeting("Hello", "Welcome")
    print(greet.show_greeting())

    condition = Condition()
    user_data1 = condition.head_condition()
    print(f"\nMental Condition : {user_data1}")

    # Save to JSON
    user_data = {"Mental Condition": user_data1}
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

    # Save to Database
    db = DataManager()
    db.save_to_db(user_data1[0], user_data1[1])
    db.close()

    # Fetch health tip from API
    tip = fetch_health_tip()

    print(f"""\nProfile Summary
    Head Condition : {user_data1}
    Health Tip (API): {tip}
    """)

    print("Data has been saved in 'user_data.json' and database 'user_data.db'")
