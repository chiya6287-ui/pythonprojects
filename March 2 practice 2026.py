import json
import time
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Condition:
    def head_condition(self):
        attempts = 0
        while True:
            try:
                feel = input("\nEnter what you are feeling (mental stress, mental pressure, headache)?\n")

                if feel.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif feel in ["mental stress", "mental pressure", "headache"]:
                    verdict = "serious for brain", "check brain specialist"
                    return verdict
                else:
                    print("\nnot match, please choose right")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait for 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

user_data = {}

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()

condition = Condition()
user_data1 = condition.head_condition()
print(f"\nMental Condition : {user_data1}")

user_data = {"Mental Condition": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Head Conition : {user_data1}""")

print("\nData has been saved in 'March 2 practice 2026' ")