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
class User_input():
    def data_input(self):
        attempts = 0
        while  True:
            try:
                data = input("\nEnter data here (enter data here)\n")
                if data.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif type(data) == str:
                    return data
                else:
                    print("\ndata is not a string")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("not matching system data, keep trying")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i}s")
                    sys.stdout.flush()
                    time.sleep(1)
                print(f"\r can try again .... ")
                attempts = 0
user_data = {}

greet = Greeting("Hello", "Welcome")
greet.show_greeting()
user = User_input()
user_data1 = user.data_input()
print(f"\nData : {user_data1}")

user_data = {"data": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
User_Input : {user_data1}""")

print("\ndata has been saved in 'user_data.json'")

print("\nOpening X in your program ....")
webbrowser.open("https://www.X.com")