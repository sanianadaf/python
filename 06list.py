list1 = [1,2,3]
list2 = list1
list1[2] = 5
print(list1)
print(list2)

list3 = list1.copy()
print(list1)
print(list3)
list3[2] = 10
print(list1)
print(list3)

# slicing
l1 = [1,2,3,4,5]
l1[:]
print(l1)
l2 = l1[:]