import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Bonding:
    def person_bonding(self):
        attempts = 0
        category = {"introvert": "introvert", 
        "social relation": "social relation", 
        "like minded": "like minded", 
        "extrovert": "extrovert"}
        while True:
            try:
                relation = input("\nChoose your relation requirement(introvert, extrovert, like minded, social relation)\n")
                if relation.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif relation in category:
                    return category.get(relation)
                else:
                    print("\nrelation not (found / match)")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait for 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

    def mutual_goals(self):
        attempts = 0
        goals = {"own business": "own business", 
        "build own empire": "build own empire", 
        "invention": "invention"}
        while True:
            try:
                interest = input("\nWhat are mutual interests (own business, build own empire, invention)\n")
                if interest.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif interest in goals:
                    return goals.get(interest)
                else:
                    print("\ninterest not (found / match)")
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

bonding = Bonding()
user_data1 = bonding.person_bonding()
print(f"\nMutual Bonding : {user_data1}")
user_data2 = bonding.mutual_goals()
print(f"\nMutual Interest : {user_data2}")

user_data = {"Bonding": user_data1, 
"Interest": user_data2}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Person Relation : {user_data1}
Persons Mutual Interest : {user_data2}""")

print("\nData has been saved in 'March 7 practice 2026' ")

with open("user_data.json", "r") as file:
    data = json.load(file)

print("\nReading back from file:")
print(data)