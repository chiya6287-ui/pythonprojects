import time
import json
from datetime import datetime
class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Goal:
    def life_goal(self):
        attempts = 0
        while True:
            try:
                direction = input("\nWhat's direction?\n")
                if direction.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif direction in ["job", "serving", "labour"]:
                    return {"message": "this direction is good for short term in terms of getting some money for a short period of time"}
                elif direction in ["build own empire", "business", "create or invent big"]:
                    return {"message": "this is the right directions and perfect goal"}
                else:
                    print("\nput right direction will tell more accurate")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
class Opportunity:
    def social_opportunities(self):
        attempts = 0
        while True:
            try:
                goal = input("\nPut your goal here\n")
                if goal.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif goal in ["serving", "labour", "working"]:
                    oppor = {"1": "working on (malls, restuarents, fast foods)"}
                    return oppor["1"]
                elif goal in ["build own empire", "business", "create or invent big"]:
                    oppor = {"1": "big companies", "2": "big industries"}
                    return list(oppor.values())
                else:
                    print("\nplease enter goal here")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
class Wealth:
    def earning(self):
        attempts = 0
        while True:
            try:
                earning = int(input("\nHow much revenue have you been generated?\n"))
                if earning >= 500000 and earning < 1000000:
                    return {"message": "You have collected handsome amounts, enough for social survival"}
                elif earning >= 1000000 and earning < 2000000:
                    return {"message": "\nCongratulations! you have became a millionaire"}
                elif earning >= 1000000000:
                    return {"message": "Congratulations! you have became a billionaire"}
                else:
                    print("\nexact earning will decide your current social status")
                    attempts += 1
            except ValueError:
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
goal = Goal()
user_data1 = goal.life_goal()
print(f"\nLife purpose : {user_data1}")
opportunity = Opportunity()
user_data2 = opportunity.social_opportunities()
print(f"\nSocial Opportunities : {user_data2}")
wealth = Wealth()
user_data3 = wealth.earning()
print(f"\nEarning : {user_data3}")
user_data = {"Goal": user_data1, 
"Opportunity": user_data2, 
"Wealth": user_data3}
with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)
print(f"""\nProfile Summary\n
Life goal : {user_data1}
\nSocial opportunities : {user_data2}
\nWealth Collected : {user_data3}""")
print("\nData has been saved in 'user_data.json' ")