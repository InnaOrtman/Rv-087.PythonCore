# task_2
# User enters ten natural numbers greater than 2. Count how many of them are
# numbers that are multiples of 5.
"""
списки у лупах друкувати необов'язково!!
- це робиться для провірки процесу;))
"""
print("***The user must enter ten natural numbers greater than 2***")
list1 = []
list2 = []

while len(list2) != 10:
    number = int(input(f"You must enter {10 - len ( list2 )} more attempts:\n"))
    list2.append(number)

    if number % 5 == 0:
        list1.append(number)
        print(list1)
    else:
        print(list2)

print(f"From your list: {list2} - {len(list1)} NUMBERS DIVIDED BY 5 WERE INTRODUCED")
