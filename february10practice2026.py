import time
import json
from datetime import datetime
class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Transaction:
    def money_sending(self):
        attempts = 0
        while True:
            try:
                account = input("\nWhich mode of transaction?\n")
                if account.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif account in ["digital", "soft account"]:
                    microfinance = {"1": "easypaisa", "2": "jazzcash", "3": "sadapay", "4": "faisal bank"}
                    return microfinance
                else:
                    print("\nother type of account")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
    def money_receiving(self):
        attempts = 0
        while True:
            try:
                account = input("\nWhich mode of receiving?\n")
                if account.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif account in ["physical", "on branch"]:
                    bank = {"1": "HBL", "3": "UBL", "2": "MEEZAN", "4": "ASKARI", "5": "FAYSAL", "6": "NBP", "7": "BOP", "8": "B-AL-H"}
                    return bank
                else:
                    print("\nother mode of banking")
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

transaction = Transaction()
user_data1 = transaction.money_sending()
print(f"\nPayment sending : {user_data1}")
user_data2 = transaction.money_receiving()
print(f"\nPayment receiving : {user_data2}")
user_data = {"Sending": user_data1, 
"Receiving":  user_data2}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Payment Sending mode : {user_data1}
Payment Receiving mode : {user_data2}""")

print("\nData has been saved in 'user_data.json' ")