import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive

    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Diet:
    def daily_diet(self):
        attempts = 0

        while True:
            try:
                food = input("\nWhat do you take in Breakfast?\n")

                if food.isdigit():
                    raise ValueError("\ndigits are not allowed")

                elif food in ["yogurt n bread", "bread n egg", "jam n bread"]:
                    return {"message": "healthy Diet, along with milk it will be superb"}

                elif food in ["mutton n bread", "beef n bread", "steam chicken"]:
                    return {"message": "Good Diet for vitamin B & 12 (for brain)"}

                elif food in ["shakes", "fruits", "dry fruits", "juices"]:
                    return {"message": "perfect diet for night digesion, take some exercise will boost muscles"}

                else:
                    print("\nEnter food please")
                    attempts  += 1

            except ValueError as e:
                print(e)
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

diet = Diet()
user_data1 = diet.daily_diet()
print(f"\nDiet level : {user_data1}")

user_data = {"Diet": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Daily Diet : {user_data1}""")

print("\nData has been saved in 'user_data.json' ")