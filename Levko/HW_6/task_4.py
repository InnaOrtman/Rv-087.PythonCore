# task_4
# Divide the tuple into several ones, each of which contains only numbers, only letters, etc

tuple_1 = (5, "hello", 11, 6, "", "geek")
list1 = []
list2 = []

for i in tuple_1:
    if type(i) is int:
        list1.append(i)
    else:
        list2.append(i)
print(tuple(list1))
print(tuple(list2))


