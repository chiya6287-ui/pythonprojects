import requests
import json
import time
import sys
import webbrowser
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Diet:
    def morning_diet(self):
        attempts = 0
        morning_diet_data = {"bread with something": "Good and energetic", 
        "Not with bread": "Not healthy and energetic"}
        while True:
            try:
                diet = input("\nEnter your morning diet (bread with something, Not with bread)\n")
                if diet.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif diet in morning_diet_data:
                    return morning_diet_data.get(diet)
                else:
                    print("\nnot a right morning diet, but something else")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again .... ")
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
    def afternoon_diet(self):
        attempts = 0
        afternoon_diet_data = {"meat with salad n bread": "good for body muscles", 
        "eggs with salad": "another source of protein and vitamins"}
        while True:
            try:
                diat = input("\nEnter your afternoon diet (meat with salad n bread, eggs with salad)\n")
                if diat.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif diat in afternoon_diet_data:
                    return afternoon_diet_data.get(diat)
                else:
                    raise ValueError("\nnot a right afternoon diet, but something else")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again .... ")
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
    def night_diet(self):
        attempts = 0
        night_diet_data = {"fruits or juice with bread": "perfect combo for night diet", 
        "only bread": "good but not reach peak energy level", 
        "exercise with running": "super for cardio and muscles as well"}
        while True:
            try:
                diat = input("\nEnter your night die (fruits or juice with bread, only bread, exercise with running)\n")
                if diat.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif diat in night_diet_data:
                    return night_diet_data.get(diat)
                else:
                    raise ValueError("\nnot a right night diet, but something else")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
class Physical_Condition:
    def body_height(self):
        attempts = 0
        heigh = {"small": 5.5, "medium": 5.7, "large": 6.0}
        while True:
            try:
                height = input("\nEnter your height here (small, medium large)\n")
                if height.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif height in heigh:
                    return f"Your body height {heigh.get(height)} inches"
                else:
                    raise ValueError("\nnot a height unit, but something else")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts =  0
    def body_weight(self):
        attempts = 0
        while True:
            try:
                weight_input = int(input("\nEnter your weight here\n"))
                if 50 <= weight_input <= 80:
                    return f"Body weight {weight_input} is balanced weight"  
                else:
                    raise ValueError("\nweight is too low or too high")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()
diet = Diet()
user_data1 = diet.morning_diet()
print(f"\nMorning diet : {user_data1}")
user_data2 = diet.afternoon_diet()
print(f"\nAfternoon diet : {user_data2}")
user_data3 = diet.night_diet()
print(f"\nNight diet : {user_data3}")
physical = Physical_Condition()
user_data4 = physical.body_height()
print(f"\nbody height : {user_data4}")
user_data5 = physical.body_weight()
print(f"\nbody weight : {user_data5}")

user_data = {"Morning Diet": user_data1,
"Afternoon Diet": user_data2,
"Night Diet": user_data3,
"Body Height": user_data4,
"Body Weight": user_data5}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Morning Diet : {user_data1}
Afternoon Diet : {user_data2}
Night Diet: {user_data3}
Body Height : {user_data4}
Body Weight : {user_data5}""")

print("\nData has been saved in 'user_data.json'")

print("\nOpening bing in your  program ... ")
webbrowser.open("https://www.bing.com/videos/search?q=m+a+n+v+s+w+i+l+d")