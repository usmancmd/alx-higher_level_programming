#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if lastDigit > 5:
    print("Last digit of {} is {} and is greater than {}".format(number, lastDigit, 5))
elif lastDigit == 0:
    print("Last digit of {} is {} and is {}".format(number, lastDigit, 0))
elif lastDigit < 6 and not 0:
    print("Last digit of {} is {} and is less than {} and not {}".format(number, lastDigit, 6, 0))
