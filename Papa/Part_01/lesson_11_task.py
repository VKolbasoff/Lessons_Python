import random

n = int(input("Enter number of elements: "))

list = [int(random.random()*100) for i in range(0, n)]

i = 0
while i < n:
    print(list[i], end=",")
    i += 1

list = set(list)
print()

for i in list:
    print(i, end=",")
