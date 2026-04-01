import time
import json
import sys
import webbrowser
from datetime import datetime

class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Planning:
    def event_attendence(self):
        attempts = 0
        reasons = {"voluntery injury": "if apply well then well done",
        "involuntery injury": "tradition acceptance",
        "no plan or lame excuse": "lead to serious happening"}
        while True:
            try:
                action = input("\nEnter action here (voluntery injury, involuntery injury)\n")
                if action.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif action in reasons:
                    return reasons.get(action)
                else:
                    print("\naction not match or found")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                print("\n")
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
planning = Planning()
result = planning.event_attendence()
print("\nEvent Attendence :", result)
user_data = {"Event Attendence": result}
with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)
print(f"""\nProfile Summary\n
Planning : {result}""")
print("\nData has been saved in 'user_data.json'")
webbrowser.open("https://www.youtube.com/results?search_query=m+a+n+v+s+w+i+l+d")