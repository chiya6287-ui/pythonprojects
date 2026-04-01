import webbrowser
import time 
import json
import requests
import sys
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Mood:
    def day_feelings(self):
        attempts = 0
        condition = {"healthy": "Ok", "tired": "leave thinking", "depression": "take exercises", "relax": "normal"}
        while True:
            try:
                day_feeling = input("\nWhat are you feeling (healthy, tired, depression, relax)\n")
                if day_feeling.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif day_feeling in condition:
                    return condition[day_feeling]
                else:
                    print("\nday feeling did not match or found")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\r⏳ Waiting... {i} seconds")
                    sys.stdout.flush()
                    time.sleep(1)
                    attempts = 0
user_data = {}

greet = Greeting("Hello", "Welcome")
greet.show_greeting()
mood = Mood()
user_data1 = mood.day_feelings()
print(f"\nFeelings : {user_data1}")

user_data = {"Feelings": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Day Mood : {user_data1}""")
print("\nData has been saved in 'user_data.json' ")
webbrowser.open("https://www.youtube.com")