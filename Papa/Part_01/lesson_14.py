def printpython():
    print("Python")


printpython()


def sum(x, y):
    return x + y

s = sum(5, 7)
print(s)

def sub(x, y):
    return x - y

s = sub(5, 7)
print(s)

def sumprint(x, y, r = False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)
sumprint(15, 7)

print(sub(y=10, x=5))

def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s
print(bigsum(1, 4, 5, 4, 23))
