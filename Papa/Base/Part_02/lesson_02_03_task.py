lent = input("How many elements do you need: ")
list = []
for i in range(int(lent)):
    n = input("Enter element: ")
    list.extend(n)
print(list)
