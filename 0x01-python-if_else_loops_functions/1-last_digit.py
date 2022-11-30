#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = -lastDigit
print("Last digit of {} is {} and is".format(number, lastDigit))
if lastDigit > 5:
    print("greater than {}".format(5))
elif lastDigit == 0:
    print("{}".format(0))
elif lastDigit < 6 and not 0:
    print("less than {} and not {}".format(6, 0))
