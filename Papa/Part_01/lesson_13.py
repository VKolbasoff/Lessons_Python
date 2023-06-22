mydict = dict()
print(mydict)

mydict = {'Name' : 'John','Ege' : 35}
print(mydict)

mydict = dict(Name='John', Age=35, IsMale=True)
print(mydict)

print(mydict["Age"])

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'IsMale')
for key in mytuple:
    print(key, '=', mydict[key])

print()

mydict = {str(i*2): i for i in range(1, 10)}
print(mydict)

