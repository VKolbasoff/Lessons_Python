array = [1, 5, 6, 3, 8, 2.5]
for n in array:
    print(n, end=(","))

print()
str = "Python"
print(str[0])

for s in str:
    print(s, end=(" "))
print()

for s in str:
    if s == "Y":
        break
else:
    print("There is no simbol 'Y' in", str, "string.")

array = range(2, 15)
for n in array:
    print(n, end=(","))

print()

array = list(range(2, 15))
print(array[5])
for n in array:
    print(n, end=(","))

print()

array = [i * 2 for i in range(1, 10)]
print(array)

array = [i for i in range(1, 10) if i % 2 == 0]
print(array)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
n = 0
while n < 10:
    i += 2
    array[n] = i
    n += 1
print(array)
