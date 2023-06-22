list = [2, 3, 7, 54]
print(list)
list.append(76)
print(list)
list.extend([4, 7, 8])
print(list)
list.insert(0, 777)
print(list)
print(len(list))

print(list.index(54))
#print(list.index('h'))
print(list.count('h'))
print(list.count(7))

list.reverse()
print(list)

list.remove(7)
print(list)
list.pop(3)
print(list)
list.clear()
print(list)
