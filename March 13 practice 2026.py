import json
import time
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Guest:
    def guest_arrival(self):
        attempts = 0
        occasion = {
            "birth celebration": "joined on the occasion",
            "death anniversary": "should come on death's person house (according to culture)"
        }
        while True:
            try:
                event = input("\nEnter which event it is (birth celebration, death anniversary)?\n")
                if event.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif event in occasion:
                    return occasion[event]
                else:
                    print("\nevent not found or match")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again")
                print("Waiting... ", end="")
                for i in range(10, 0, -1):
                    print(f"{i} seconds remaining", end="\r")
                    time.sleep(1)
                # jab countdown khatam ho jaye to line clear kar do
                print(" " * 30, end="\r")
                attempts = 0

user_data = {}
greet = Greeting("Hello", "Welcome")
greet.show_greeting()

guest = Guest()
user_data1 = guest.guest_arrival()
print(f"Arrival Cause : {user_data1}")

user_data = {"Arrival": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Guest Arrival : {user_data1}""")

print("\nData has been saved in 'user_data.json'")
