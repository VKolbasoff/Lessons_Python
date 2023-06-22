#import random
#import math as m
from random import *
import cmath as sm

#print(random.randint(0, 10))
print(randint(5, 39))
#print(m.sin(1))
print(sm.log10(1000))
import calc


while True:
    print("1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division, 0 - Exit")
    code = input("Enter command:")
    if code == "0":
        exit(0)
    a = float(input("Enter first digit: "))
    b = float(input("Enter second digit: "))
    if code == "1":
        r = calc.sum(a, b)
    elif code == "2":
        r = calc.sub(a, b)
    elif code == "3":
        r = calc.mult(a, b)
    elif code == "4":
        r = calc.div(a, b)
    print("Result:", r)
