#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 or number > 0:
    temp = number
    if temp < 0:
        temp = -temp
    if temp % 10 == 0:
        print(f"Last digit of {number:d} is {temp % 10} and is 0")
    elif temp % 10 > 5:
        print(f"Last digit of {number:d} is {temp % 10} and is greater than 5")
    elif temp % 10 < 6:
        print(f"""
Last digit of {number:d} is {temp % 10} and is less than 6 and not 0""")
