import time
import json
from datetime import datetime
from math import sqrt
class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive

    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")

class Calculator:
    def addition(self):
        attempts = 0

        while True:
            try:
                n1 = int(input("\nEnter first number\n"))
                n2 = int(input("\nEnter second number\n"))
                n3 = n1 + n2
                n4 = sqrt(n1)
                return {"sum is": n3, "and sqrt is": n4}

            except ValueError as e:
                print(e)
                print("\nput the right data")
                attempts += 1

            if attempts >= 3:
                print("\nplease wait for 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

    def subtraction(self):
        attempts = 0

        while True:
            try:
                n1 = int(input("\nEnter first number\n"))
                n2 = int(input("\nEnter second number\n"))
                n3 = n1 - n2
                return {"subtract is": n3}

            except ValueError as e:
                print(e)
                print("\nkeep trying")
                attempts += 1
            
            if attempts >= 3:
                print("\nplease wait 10 seconds before tying again ..... ")
                time.sleep(10)
                attempts = 0

    def product(self):
        attempts = 0

        while True:
            try:
                n1 = int(input("\nEnter first number\n"))
                n2 = int(input("\nEnter second number\n"))
                n3 = n1 * n2
                return {"multiplication": n3}

            except ValueError as e:
                print(e)
                print("\nkeep Trying")
                attempts += 1

            if attempts >= 3:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

    def quotient(self):
        attempts = 0

        while True:
            try:
                n1 = int(input("\nEnter first number\n"))
                n2 = int(input("\nEnter second number\n"))
                n3 = n1 / n2
                return {"division is": n3}

            except ZeroDivisionError:
                print("\nDivision by zero is not working")
                attempts += 1

            if attempts >= 3:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0

user_data = {}

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()

calculator = Calculator()
user_data1 = calculator.addition()
print(f"\nsum result : {user_data1}")

user_data2 = calculator.subtraction()
print(f"\nsubtraction result : {user_data2}")

user_data3 = calculator.product()
print(f"\nmultiplication result : {user_data3}")

user_data4 = calculator.quotient()
print(f"\ndivision result : {user_data4}")

user_data = {"Addition":user_data1, 
"Subtraction":user_data2, 
"Multiplication":user_data3, 
"Division":user_data4}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Addition : {user_data1}
Subtraction : {user_data2}
Product : {user_data3}
Quotient : {user_data4}""")

print("\nData has been saved in 'user_data.json' ")