import time
import json
import sys

class Physical_Condition:
    def body_weight(self):
        attempts = 0
        while True:
            try:
                weight_input = input("\nEnter your weight here\n")
                weight_input = int()
                if type(weight_input) == str:
                    raise ValueError("\nStrings are not allowed")
                if not (50 <= weight_input <= 80):
                    raise ValueError("\nweight is too low or too high")
                elif not weight_input.isalpha():
                    return (f"Body weight {weight_input} is balanced weigh")
                else:
                    raise ValueError("\nThis is somethig else not weigh")
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
physical = Physical_Condition()
physical.body_weight()