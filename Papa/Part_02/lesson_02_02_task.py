string = input("Enter string: ")

for i in string:
    print(ord(i))

digit = input("Enter only digits: ")

try:
    digit = int(digit)
    print("Thank you!")
except ValueError:
    print("Incorrect input!")





