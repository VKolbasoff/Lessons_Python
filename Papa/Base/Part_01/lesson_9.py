list = []
print(list)
list = ['h', 'e', 'l', 'l', 'o']
print(list)

print(list[0])
print(list[4])
print("Last element:", list[-1])
print("List length:", len(list))
print("Last element:", list[len(list) - 1], "\n")

i = 0
while i < len(list):
    print(list[i], end=", ")
    i += 1
print("\n")

list[1] = 78
print(list[1])
print(list)
print(list[len(list)-1])
print("\n")

list = [[2, 6, "r"], 5, "btr"]
print(list[0][1], end=", ")
print(list[-1])

list = [[0, 1], [2, 3, 4]]
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
            print(list[i][j], end=", ")
            j += 1
    i += 1

print("\n")
prices = [20, 30, 50, 10, 44]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print(min, max)








