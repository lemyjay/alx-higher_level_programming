#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number)
neg = "-" if number < 0 else ""
lt = temp % 10
if lt == 0:
    print(f"Last digit of {number} is {neg}{lt} and is 0")
elif lt > 5:
    print(f"Last digit of {number} is {neg}{lt} and is greater than 5")
else:
    print(f"Last digit of {number} is {neg}{lt} and is less than 6 and not 0")
