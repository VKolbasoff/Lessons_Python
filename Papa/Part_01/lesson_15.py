def sums(x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s


def sub(x, y):
    global result
    result = float(x) - float(y)


result = 0

isprint = False
x = input("Enter digit 1:")
y = input("Enter digit 2:")
print("The sum is:", sums(x, y))
sub(x, y)
print("The difference is:", result)
