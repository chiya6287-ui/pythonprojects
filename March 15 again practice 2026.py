import time
import json
import webbrowser
import requests
import sys
from datetime import datetime
class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Portfolio:
    def event_importance(self):
        attempts = 0
        value = {"happy event": "give priority to every one", 
        "sad event": "neglect priority concept"}
        while True:
            try:
                event = input("\nEnter event here (happy event, sad event)\n")
                if event.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif event in value:
                    return value.get(event)
                else:
                    print("\nEvent not found or match")
                    attempts += 1
            except ValueError as e:
                print(e)
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i}s")
                    sys.stdout.flush()
                    time.sleep(1)
                print(f"\rNow keep try again ...")
                attempts = 0
    def class_portfolio(self):
        attempts = 0
        portfolio = {"elite class": "give special protocols", 
        "upper middle class": "give protocols", 
        "middle class": "give priority", 
        "others": "adjust in event"}
        while True:
            try:
                clas = input("\nEnter class here (elite class, upper middle class, middle class, others)\n")
                if clas.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif clas in portfolio:
                    return portfolio.get(clas)
                else:
                    print("\nevent did not match or found")
                    attempts += 1
            except ValueError as e:
                print(e)
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i}s")
                    sys.stdout.flush()
                    time.sleep(1)
                print(f"\r Again keep trying")
                attempts = 0
user_data = {}
print("\n", datetime.now())
greet = Greeting("Hello", "Welcome")
greet.show_greeting()
portfolio = Portfolio()
user_data1 = portfolio.event_importance()
print(f"\nEvent : {user_data1}")
user_data2 = portfolio.class_portfolio()
print(f"\nClass : {user_data2}")

user_data = {"Event": user_data1,
"Class": user_data2}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Event importance : {user_data1}
Class importance : {user_data2}""")
print("\nData has been saved in 'user_data.json'")
print("\nOpening instagram in your program ... ")
webbrowser.open("https://www.instagram.com")