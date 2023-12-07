list1=[1, 2, 3]
list2=['abc', 'def', 'ghi']
list3=['1', '2', 'ab', 'cd']
list4=['1','2','3','4']

print(len(list1))
print(list1.count(1))
print(list1.extend(list2))
list1.append(list2)
list1.insert(2, 8)
print(list1)
