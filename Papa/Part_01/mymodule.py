def mymax(*mylist):
    r = 0
    for i in mylist:
        if i > r:
            r = i
    print(r)

def mymin(*mylist):
    r = mylist[0]
    for i in mylist:
        if r > i:
            r = i
    print(r)

def mysum(*mylist):
    r = 0
    for i in mylist:
        r = r + i
    return r









