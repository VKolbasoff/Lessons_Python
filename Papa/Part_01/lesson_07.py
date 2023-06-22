print("Enter 0,1 or 2:")
a = input()

if a == "0":
    print("You entered 0.")
    print("This digit is less then 10.")
elif a == "1":
    print("You entered 1.")
elif a == "2":
    print("You entered 2.")
else:
    print("Incorrect input!")

cond = a == "0" or a == "1" or a == "2"
if cond:
    x = 0
else:
    x = 3
print("x = ", x, cond)

x = 0 if cond else 3
print("x = ", x, cond)






