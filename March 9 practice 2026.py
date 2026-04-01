import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Ethics:
    def social_ethics(self):
        attempts = 0
        respect = {1: "world arrival", 2: "world exit", 3: "social trajedy", 4: "social happy"}
        while True:
            try:
                ethic = int(input("\nEnter Ethic here (1, 2, 3, 4)\n"))
                if ethic in respect:
                    return respect[ethic]
                else:
                    print("\nethic not match / found")
                    attempts += 1
            except ValueError:
                print("\nOnly numbers 1-4 are allowed")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

user_data = {}

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()

ethics = Ethics()
user_data1 = ethics.social_ethics()
print(f"\nEthics : {user_data1}")

user_data = {"Ethics": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Social Ethics : {user_data1}""")

print("\nData has been saved in 'user_data.json' ")