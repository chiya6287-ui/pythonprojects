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
class Meal:
    def day_meal(self):
        attempts = 0
        routine = {
            "morning": "breakfast",
            "afternoon": "Lunch",
            "night": "dinner",
            "late night": "anything that will boost energy"
        }
        while True:
            try:
                condition = input("\nPut condition here (morning, afternoon, night, late night)\n")
                if condition.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif condition in routine:
                    return routine[condition]
                else:
                    print("\ncondition did not match or found")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\n")
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i} seconds")
                    sys.stdout.flush()
                    time.sleep(1)
                print("\r✅ You can try again now!     ")
                attempts = 0
class Sleep:
    def sleeping_hours(self):
        attempts = 0
        feedback = {
            "9pm-4am": "perfect sleep hours",
            "9pm-5am": "good sleep hours",
            "10pm-3am": "not enough",
            "2am-7am": "dangerous for brain"
        }
        while True:
            try:
                sleep = input("\nPut your sleeping time here (9pm-4am, 9pm-5am, 10pm-3am, 2am-7am)\n")
                if sleep.isdigit():
                    raise ValueError("\nDigits are not allowed")
                elif sleep in feedback:
                    return feedback[sleep]
                else:
                    print("\nsleep time did not match")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1

            if attempts >= 2:
                print("\nToo many wrong attempts, please wait...")
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i} seconds")
                    sys.stdout.flush()
                    time.sleep(1)
                print("\r✅ You can try again now!     ")
                attempts = 0
                
user_data = {}
print("\n", datetime.now())
greet = Greeting("Hello", "Welcome")
greet.show_greeting()
meal = Meal()
user_data1 = meal.day_meal()
print(f"\nMeal : {user_data1}")
sleep = Sleep()
user_data2 = sleep.sleeping_hours()
print(f"\nSleeping : {user_data2}")
user_data = {"Meal": user_data1, 
"Sleeping": user_data2}
with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)
print(f"""\nProfile Summary\n
Day Meal : {user_data1}
Sleeping Hours : {user_data2}""")
print("\nData has been saved in 'user_data.json'")
print("Opening google in your program ...")
webbrowser.open("https://www.google.com")