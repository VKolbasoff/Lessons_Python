def even(y):
    mos = y % 2 == 0
    return mos

def maxnum(x, y, z):
    if x > y and x > z:
        max = x
    elif y > z:
        max = y
    else:
        max = z
    return max

def armean(*mylist):
    n = 0
    t = 0
    for i in mylist:
        n = n + i
        t += 1
    armm = n/t
    return armm

print(even(5))

print(maxnum(3, 5, 6))

print(armean(5, 3, 6, 12))

