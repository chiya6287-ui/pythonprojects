import time
import json 
from datetime import datetime
from math import sqrt
from math import log

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Chart:
    def sales_sum(self):
        while True:
            try:
                firstsale = int(input("\nEnter first month sale here\n"))
                secondsale = int(input("\nenter second month sale here\n"))
                firstmonthchart = firstsale + secondsale
                sqrtfirstsale = sqrt(firstsale)
                return {"month sale": sqrtfirstsale, "first month chart": firstmonthchart}
            except ValueError:
                print("\nkeep trying")
    def sales_chart(self):
        attempts = 0
        while True:
            try:
                sale = input("\nEnter monhly sale here\n")
                if sale.isdigit():
                    sale = int(sale)
                if sale < 50000:
                    salechart = log(1)
                elif sale < 50000:
                    salechart = log(1)
                    print({"this month sales chart is": salechart})
                else:
                    raise ValueError("strings are not allowed")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again .....")
                time.sleep(10)
                attempts = 0
user_data = {}

print("\n", datetime.now())

greet = Greeting("Hello", "Welcome")
greet.show_greeting()

chart = Chart()
user_data1 = chart.sales_sum()
print(f"\nMonth sale : {user_data1}")
user_data2 = chart.sales_chart()
print(f"\nMonth sale chart : {user_data2}")

user_data = {"Month sale": user_data1, 
"Month sale chart": user_data2}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Month sale : {user_data1}
Month sale chart : {user_data2}""")

print("\nData has been saved in 'user_data.json' ")