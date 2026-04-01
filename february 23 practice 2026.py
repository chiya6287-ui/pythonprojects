import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class MentalC:
    def behaviour(self):
        attempts = 0
        while True:
            try:
                emotion = input("\nEnter your emotion here (happy, sad, angry, tired)\n")
                if emotion in ["sad", "angry", "tired"]:
                    return "condition may go under emotions"
                else:
                    print("\nemotion will decide, put it")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("\nnot an emotion")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
user_data = {}

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()
mental = MentalC()
user_data1 = mental.behaviour()
print(f"\nMental Condition : {user_data1}")

user_data = {"Mental": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Brain Health : {user_data1}""")

print("\nData has been saved in 'user_data.json' ")