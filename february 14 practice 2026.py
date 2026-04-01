import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class BirthDayWish:
    def celebration(self):
        attempts = 0
        day = {"on day": "birthday celebrated", 
        "not on day": "birthday not celebrated"}
        while True:
            try:
                arrival = input("\nEnter Arrival of guests (on day, not on day)\n")
                if arrival.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif arrival in day:
                    return day[arrival]
                else:
                    print("\nDid not choose right, please choose the right one")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
user_data = {}

print("\n", datetime.now())
greet = Greeting("Hello", "Welcome")
greet.show_greeting()
birthday = BirthDayWish()
user_data1 = birthday.celebration()
print(f"\nCelebration day : {user_data1}")

user_data = {"day": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
BirthDayWish : {user_data['day']}""")

print("\nData has been saved in 'user_data.json' ")