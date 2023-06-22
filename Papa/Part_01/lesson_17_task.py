a = input("Enter fist number: ")
b = input("Enter second number: ")

try:
    print(float(a)/float(b))
except ZeroDivisionError:
    print("Infinity!")


