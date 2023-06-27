def printdict(**dict):
    for key in dict:
        print(key,"=", dict[key])

def getmax(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

printdict(name='Ivan', age=15)

# Anon functions

lambdafunc = lambda x, y: print(x + y)
lambdafunc(5, 7)

print((lambda x, y: x + y) (1, 5))

result = ((lambda x, y: x + y) (5, 5))
print(result)

print(getmax([3, 6, 8, 34, 9]))
print(getmax([3, 87, 8, 74, 5]))
