s1 = "String"
s2 = "Variable"

print(len(s1))
print(s1[1])
print(s1[-1])
print(s2[-2])
print(s2[1:4])

s3 = "abc\nxyz"
s4 = r"abc\nxyz"  # Модификатор r все спецсимволы не обрабатываются

print(s3)
print(s4)

s5 = "Hello"
print(s5 * 2)

print(s1.find("i"))  # Возвращает номер буквы
print(s1.find("i", 2))  # Возвращает номер буквы начиная с указанного символа

print(s2.isdigit()) # Проверяет на наличие цифр
print(s2.isalpha()) # Проверяет на наличие букв

print(s5.upper())
print(s5.lower())

print(ord("a"))
print(chr(97))

s6 = "     Tr   "
print(s6)
print(s6.strip())

s7 = "Hello, {0}. Your age is {1}."
print(s7.format('Alex', 30))

s8 = "Hello, {name}, Your age is {age}."
print(s8.format(name='Alex', age=30))

data = ('Alex', 30)
s9 = "Hello, {0[0]}. Your age is {0[1]}."
print(s9.format(data))









