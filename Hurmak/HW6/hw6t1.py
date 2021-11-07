import random


list1 = []
list2 = []
list3 = []
for i in range(0, random.randint(1, 10)):
    list1.append(random.randint(1, 10))
    list2.append(int(input('Enter number: ')))
    list3.append(list1[i] + list2[i])
print(list1)
print(list2)
print(list3)
