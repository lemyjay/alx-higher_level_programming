#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number)
sign = "-" if number < 0 else ""
ldigit = temp % 10
if ldigit == 0:
    print(f"Last digit of {number} is {sign}{ldigit} and is 0")
elif ldigit > 5:
    print(f"Last digit of {number} is {sign}{ldigit} and is greater than 5")
else:
    print(f"Last digit of {number} is {sign}{ldigit} and is less than 6 and not 0")
