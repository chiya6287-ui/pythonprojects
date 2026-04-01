import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Skill:
    def driving_skill(self):
        attempts = 0
        while True:
            try:
                desire = input("\nWhich skill do you want?\n (bike, car, truck, 22 wheel)\n")
                if not desire.isdigit():
                    desir = ["bike", "car", "truck", "22 wheel"]
                    return {"you want to learn the skill of": desir}
                else:
                    print("\ndesire did not match")
                    attempts += 1
            except ValueError:
                print("\nkeep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait for 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
    def skill_certificate(self):
        attempts = 0
        while True:
            try:
                duration = int(input("\nHow many days have you been completed for skill so far?(5, 12, 14)\n"))
                if duration in [5, 12, 14]:
                    return {"1": "bike skill take 5 days", "2": "car skill take 12 days", "3": "truck skill take 14 days"}
                else:
                    print("\nSkill duration not match")
                    attempts += 1
            except ValueError:
                print("\nkeep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

user_data = {}

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()
skill = Skill()
user_data1 = skill.driving_skill()
print(f"\nSkill level : {user_data1}")
user_data2 = skill.skill_certificate()
print(f"\nCompletion certificate : {user_data2}")

user_data = {"Skill": user_data1,
"Certificate": user_data2}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Skill Category : {user_data1}
Skill Award : {user_data2}""")

print("\nData has been saved in 'user_data.json' ")
                