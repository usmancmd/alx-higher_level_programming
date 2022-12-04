#!/usr/bin/python3
if __name__ == "__main__":
	import sys
from calculator_1 import add, sub, mul, div

i = len(sys.argv) - 1

if i != 3:
	print("Usage: ./100-my_calculator.py <a> <operator> <b>")
	sys.exit(1)

opt = sys.argv[2]
if opt != "+" and opt != "-" and opt != "*" and opt != "/":
	print("Unknown operator. Available operators: +, -, * and /")
	sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

if opt == "+":
	print("{} + {} = {}".format(a, b, add(a, b)))
elif opt == "-":
	print("{} - {} = {}".format(a, b, sub(a, b)))
elif opt == "*":
	print("{} * {} = {}".format(a, b, mul(a, b)))
elif opt == "/":
	print("{} / {} = {}".format(a, b, div(a, b)))

		
