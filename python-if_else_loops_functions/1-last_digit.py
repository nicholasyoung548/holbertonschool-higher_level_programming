#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastd = number % 10
elif number < 0:
    lastd = (((number * -1) % 10) * -1)
if lastd < 6 and lastn != 0:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
elif lastd == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
