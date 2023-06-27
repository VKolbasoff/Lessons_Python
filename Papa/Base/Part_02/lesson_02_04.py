set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4}
print(len(set_1))

set_1.add(10)
print(set_1)

set_1.remove(10)
print(set_1)

#set_1.remove(5)
set_1.discard(5)
print(set_1)

print(set_1 == set_2)
print(set_1 <= set_2)
print(set_1 >= set_2)

set1 = {2, 3, 4}
set2 = {1, 2, 3}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
set1.clear()
set2.clear()
print(set1)
print(set2)






