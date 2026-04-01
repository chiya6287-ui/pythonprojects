import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive

    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Workout:
    def daily_workout(self):
        attempts = 0

        while True:
            try:
                exercise = input("\nPut Exercise here\n")

                if exercise.isdigit():
                    raise ValueError("\ndigits are not allowed")

                elif exercise in ["pushups", "squats", "plank"]:
                    return {"message": "first week body warm up"}

                else:
                    print("\nExercise not match")
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

workout = Workout()
user_data1 = workout.daily_workout()
print(f"\nExercise level : {user_data1}")

user_data = {"exercise level": user_data1}

with open("user_data.json", "w")as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Daily Exercise level : {user_data1}""")

print("\nData has been saved in 'user_data.json' ")