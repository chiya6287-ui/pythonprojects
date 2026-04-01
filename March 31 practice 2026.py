import time
import json
from datetime import datetime
import sys
import webbrowser
class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Connection:
    def first_meetup(self):
        attempts = 0
        connect = {"boy to girl":  "he should attentive & active", 
        "girl to boy": "she should straight forward", 
        "both in a group": "they should make a healthy discussion in group"}
        while True:
            try:
                meetup = input("\nWho did meet first? (boy to girl,  girl to boy, both in a group)\n")
                if meetup.isdigit():
                    raise ValueError("\ndigits  are not allowed")
                elif meetup in connect:
                    return {f"first move is from {meetup} and":connect.get(meetup)}
                else:
                    print("\nmeetup did not match or found")
                    attempts+=1
            except ValueError as e:
                print(e)
                print("keep trying")
                print("\n")
                attempts+=1
            if attempts>=2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
                print("\n")
class Relation_Ship:
    def relation_ship_time(self):
        attempts = 0
        relation_ship = {"one week": "both have known some key facts about each other", 
        "two weeks": "if their bonding is good then both are nearly to close in relation",
        "one month": "if both are still in good relation then gradually they are close with each other"}
        while True:
            try:
                duration = input("\nHow much time did you spent each other? (one week, two weeks, one month)\n")
                if duration.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif duration in relation_ship:
                    return{f"Their relation_ship_time is {duration} and":relation_ship.get(duration)}
                else:
                    print("\nduration did not match or found")
                    attempts+=1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts+=1
                print("\n")
            if attempts>=2:
                for i in range(10, 0,  -1):
                    sys.stdout.write(f"\rWaiting {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
                print("\n")
class Psyche:
    def ideas(self):
        attempts = 0
        minds = {"both traditional": "just acceptable for social dealings",
        "one traditional one out of the box": "both should explain their ideas and connect at same point with hapiness",
        "both out of the box": "Life is extraordinary and peaceful for both"}
        while True:
            try:
                idea = input("\nwhat type of both of you? (both traditional, one traditional one out of the box, both out of the box)\n")
                if idea.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif idea in minds:
                    return{f"Individuals thinking are {idea} and": minds.get(idea)}
                else:
                    print("\nidea did not match or found")
                    attempts+=1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts+=1
                print("\n")
            if attempts>=2:
                for i in range(10, 0, -1):
                    sys.stdout.write(f"\rWaiting {i} s")
                    sys.stdout.flush()
                    time.sleep(1)
                attempts = 0
                print("\n")

print("\n", datetime.now())
greet = Greeting("Hello", "Welcome")
greet.show_greeting()
connection = Connection()
user_data1 = connection.first_meetup()
print(f"\nfirst meetup : {user_data1}")
relation = Relation_Ship()
user_data2 = relation.relation_ship_time()
print(f"\nrelation time : {user_data2}")
psyche = Psyche()
user_data3 = psyche.ideas()
print(f"\nthinking : {user_data3}")
user_data = {"meetup": user_data1,
"relation": user_data2,
"thinking": user_data3}
with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)
print(f"""\nProfile Summary\n
Individuals_meetup : {user_data1}
Individuals_relation_time : {user_data2}
Individuals_thinking : {user_data3}""")
print("\nData has been saved in 'user_data.json'")
webbrowser.open("https://www.istagrma.com/videos?q=S+p+a+c+e+X")