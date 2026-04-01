import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive

    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Routine:
    def daily_routine(self):
        attempts = 0

        while True:
            try:
                routine = input("\nEnter Daily Routine\n")

                if routine.isdigit():
                    raise ValueError("\ndigits are not allowed")

                elif routine in ["bread n omlet", "milk and yogurt", "fruits"]:
                    return {"message": "breakfast  time"}

                elif routine in ["chicken n bread", "mutton n bread", "beef n bread"]:
                    return {"message": "lunch time"}

                elif routine in ["barbq", "burger n pizza", "jung food"]:
                    return {"message": "dinner time"}

                else:
                    print("\nIt is odd, put right option")
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

routinee = Routine()
user_data1 = routinee.daily_routine()
print(f"\nRoutine : {user_data1}")

user_data = {"Routine": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Daily Routine : {user_data1}""")

print("\nData has been saved in 'user_data.json' ")