list = ["А", "ри", "зо", "н", "а"]

i = 0
while i < len(list):
    print(i, "-", list[i])
    i += 1


a = int(input("Enter number of element: "))

if a > 1 and a < 6:
    print(list[a-1])
else:
    print("There is no element with this number!")
