import time
import json
from datetime import datetime
class Greeting:
    def __init__(self, greet, receive):
        self.greet = greet
        self.receive = receive
    def show_greeting(self):
        print(f"\n{self.greet} & {self.receive}")
class Problem:
    def machine_problem(self):
        attempts = 0
        while True:
            try:
                error = input("\nEnter error  (hardware issue, software issue, internet problem)\n")
                if error.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif error in ["hardware issue", "software issue", "internet problem"]:
                    return {"message": "error is from technology"}
                else:
                    print("\nerror did not match, please enter the matching error")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
class Solution:
    def machine_solution(self):
        attempts = 0
        while True:
            try:
                error = input("\nEnter your choosen error  (hardware issue, software issue, internet problem)\n")
                if error.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif error == "hardware issue":
                    sol = {"1": "computer laboratories", "2": "big computer manufacturing industries"}
                    return list(sol.values())
                elif error == "software issue":
                    sol = {"1": "software houses", "2": "software experts"}
                    return list(sol.values())
                elif error == "internet problem":
                    sol = {"1": "network agencies", "2": "network expert"}
                    return list(sol.values())
                else:
                    print("\nprobably you did not choose the matching error, please choose the matching one")
                    attempts += 1
            except ValueError as e:
                print(e)
                print("keep trying")
                attempts += 1
            if attempts >= 2:
                print("\nplease wait 10 seconds before trying again ..... ")
                time.sleep(10)
                attempts = 0
class Feedback:
    def feedbac(self):
        attempts = 0
        while True:
            try:
                response = input("\nGive your feedback\n")
                if response.isdigit():
                    raise ValueError("\ndigits are not allowed")
                elif response in ["good", "best", "better"]:
                    return {"message": "Thanks for your giving response '😊'"}
                elif response in ["average", "bad", "worst"]:
                    return {"message": "we respect your feelings and will improve more next time"}
                else:
                    print("\nnot a response, giving feedback will make warm relation with us")
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
problem = Problem()
user_data1 = problem.machine_problem()
print(f"\nProblem is : {user_data1}")
solution = Solution()
user_data2 = solution.machine_solution()
print(f"\nSolution is : {user_data2}")
feedback = Feedback()
user_data3 = feedback.feedbac()
print(f"\nResponse is : {user_data3}")

user_data = {"Problem": user_data1, 
"Solution": user_data2, 
"Response": user_data3}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)

print(f"""\nProfile Summary\n
Problem detect : {user_data1}
Solution recommand : {user_data2}
Feedback : {user_data3}""")

print("\nData has been saved in 'user_data.json' ")