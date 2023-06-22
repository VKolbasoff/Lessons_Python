mydict = {'Name': 'Без имени', 'Age' : -1}
name = input("Введите ваше имя:")
age = input("Введите ваш возраст:")

mydict = dict(Name=name, Age=age)
for i in mydict:
    print(mydict[i])

