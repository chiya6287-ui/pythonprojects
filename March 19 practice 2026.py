import json
import time
import sys
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Person_Profile:
    def name(self):
        attempts = 0
        while True:
            try:
                name = input("\nEnter Name\n")
                if name.isdigit():
                    raise ValueError("\nDigits are not allowed")
                if not (3 <= len(name) <= 50):
                    raise ValueError("\nName length too short or too long")
                if not name.replace(" ", "").isalpha():
                    raise ValueError("\nOnly alphabets are allow")
                return name
            except ValueError as e:
                print(e)
                print("keep trying\n")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rwait {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
    def email(self):
        attempts = 0
        email = "user@example.com"
        while True:
            try:
                email = input("\nEnter email (email contain '@' and '.')\n")
                if "@" in email and "." in email:
                    return email
                else:
                    raise ValueError("\nInvalid email format")
            except ValueError as e:
                print(e)
                print("\nkeep trying")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
    def age(self):
        attempts = 0
        while True:
            try:
                age = int(input("\nEnter age\n"))
                if not (18 <= age <= 99):
                    raise ValueError("\nAge must be between 18 and 99")
                return age
            except ValueError:
                print("\nkeep trying")
                attempts += 1
            if attempts >= 2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWait {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0

print("\n", datetime.now())
greet = Greeting("Hello", "Welcome")
greet.show_greeting()
person = Person_Profile()
user_data1 = person.name()
print(f"\nName : {user_data1}")
user_data2 = person.email()
print(f"\nEmail : {user_data2}")
user_data3 = person.age()
print(f"\nAge : {user_data3}")

user_data = {"Name": user_data1,
"Email": user_data2,
"Age": user_data3}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
User Name : {user_data1}
User Email : {user_data2}
User Age : {user_data3}""")
print("\nData has been saved in 'user_data.json'")

