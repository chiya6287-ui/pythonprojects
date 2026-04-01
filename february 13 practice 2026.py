import time
import json
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self .greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Birthday:
    def day_celebration(self):
        attempts = 0
        celebration = {"13 july": "-> 13 JULY IS AROOSA'S BIRTHDAY", 
        "13 february": "-> 13 FEBRUARY IS AITZAZ'S BIRTHDAY", 
        "1 july": "-> 1 JULY IS ZAWWAR'S BIRTHDAY"}
        while True:
            try:
                day = input("\nEnter day\n")
                if day.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif day in celebration:
                    return celebration[day]
                else:
                    print("\ndate not match please try again")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
    def celebration_gift(self):
        attempts = 0
        celebration = {"money": "-> cash money beneficial for buying", 
        "not dress shirt": "-> clothes best for light dress", 
        "dress pent shirt": "-> best gift for events", 
        "prayer": "-> belief's  prayer helps for hard time", 
        "cake": "-> basic thing of celebration"}
        while True:
            try:
                gift = input("\nWhat gift is? (cash money, clothes, dress pant shirt, prayers, cake)\n")
                if gift.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif gift in celebration:
                    return celebration[gift]
                else:
                    print("\nprobably it is not a gift please give the matching gift")
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

birthday = Birthday()
user_data1 = birthday.day_celebration()
print(f"\nDay is : {user_data1}")

user_data2 = birthday.celebration_gift()
print(f"\ncelebration is : {user_data2}")

user_data = {"Day": user_data1, 
"Celebration": user_data2}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Special Day : {user_data['Day']}
Special celebration gift ; {user_data['Celebration']}""")

print("\nData has been saved in 'user_data.json' ")
