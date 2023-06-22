import random

myset = set()
print(myset)
myset = {}
print(myset)

myset = set("Python")
print(myset)

myset = {'1', 2, 44.3, 'rt', 2}
print(myset)

list = [i for i in range(0, 10)]
print(list)
myset = set(list)
print(myset)

print(int(random.random() * 10))

mylist = (4, 4, 5)
print(mylist)


arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
arr = set(arr)
print(arr)
