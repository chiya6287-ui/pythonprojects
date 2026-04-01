import json
import time
from datetime import datetime
import requests 

url = "https://api.open-meteo.com/v1/forecast?latitude=31.5497&longitude=74.3436&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"{self.greet} & {self.receive}")

class Psyche:
    def experience_psyche(self):
        attempts = 0
        while True:
            try:
                dic = {"positive": "mature", "negative": "cruel", "neutral": "emotional"}
                experience = input("\nEnter your experience with others (positive, negative, neutral)\n")
                if experience.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif experience in dic:
                    return dic[experience]
                else:
                    print("\nexperience not found or match")
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
psyche = Psyche()
user_data1 = psyche.experience_psyche()
print(f"\nBonding : {user_data1}")

user_data = {"Bonding": user_data1}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Psyche Experience : {user_data1}""")

print("\nData has been saved in 'user_data'")


