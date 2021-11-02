# Task 6
# For user-entered numbers, determine the percentage of positive and negative
# numbers. When entering the number 0, finish the job.
print("The user must enter the numbers to determine the percentage of positive and negative numbers!\n!!!Enter 0 if you want to finish and find out the result!!!")

list1 = []
list2 = []
list3 = []
a = True

while True:
    number = int(input("Enter the number: "))
    list3.append(number)
    if number > 0:
        list1.append(number)
    elif number < 0:
        list2.append(number)
    elif number == 0:
        del list3[-1]
        print(list3)
        break

print(f"The percentage of positive numbers is: {round(len(list1)*100/len(list3))} %")
print(f"The percentage of negative numbers is: {round(len(list2)*100/len(list3))} %")

