i = 0
while i < 10:
    i += 1
    print("Hello", i)
print("The cycle is completed.\n")

i = int(input("Enter varialble less then 3:"))
while i < 10:
    i += 1
    if i == 3:
        print("I = 3")
        continue
    if i == 8:
        break
    print(i)
print("The cycle is completed.\n")

s = 0
to = 10
summa = 0
while s < to:
    s += 1
    summa = summa + s
    print(summa, s)
print("Sum of digits from 1 to", to, "equal:", summa)

while True:
    code = input("Enter 0 for exit.")
    if code == "0":
        break
exit(0)



