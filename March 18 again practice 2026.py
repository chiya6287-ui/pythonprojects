import webbrowser
import sys
import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Month:
    def march(self):
        attempts = 0
        while True:
            try:
                earn = input("\nEnter this month sale\n")
                if earn.isdigit():
                    raise ValueError("\ndigits are not allowed")
                if not (3 <= len(earn) <= 30):
                    raise ValueError("\nInput length must be between 3 and 30 characters")
                if not earn.isalpha():
                    raise ValueError("\nOnly alphabetic characters allowed")
                return earn

            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i}s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()

month = Month()
user_data1 = month.march()
print(f"\nEarn : {user_data1}")

user_data = {"Earn": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Monthly Earn : {user_data1}""")
print("\nData has been saved in 'user_data.json'")

print("\nOpening Linkedin in your program ... ")
webbrowser.open("https://www.linkedin.com")