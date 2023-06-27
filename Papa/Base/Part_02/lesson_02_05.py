d = {'Name': 'Vova', 'Age': 47}
print(d)

d.setdefault('Is working', True)
print(d)

print(d.get('Age'))

d.pop('Name')
print(d)

print(list(d.keys()))

keys = list(d.keys())
print(keys)

values = list(d.values())
print(values)

d['Age'] = 40
d['IsMale'] = True
print(d)

d.clear()
print(d)
