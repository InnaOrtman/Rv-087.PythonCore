# task_1
import random

list1 = []
list2 = []
list3 = []
c = 6
for i in range(1, c):
    list1.append(random.randint(1, 100))
print(f"Random list: {list1}")

for i in range(1, c):
    try:
      x = int(input("Enter 5 numbers, please: "))
      list2.append(x)
    except:
        print("Enter only numbers, please")
        exit()

n = 0
for i in range(1, c):
    y = list1[n] + list2[n]
    list3.append(y)
    n += 1
print(f"random list: {list1}\nYour list: {list2}\nrandom list + your list = {list3}\n")
