pi = 3.141592
square = 0


def sqr(r):
    global square
    square = pi * r ** 2


r = float(input("Enter radius:"))
sqr(r)
print("Square is:", square)
