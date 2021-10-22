# task_3

qustion = int(input("Enter the number from -99 to 99, please: "))

if 10 > qustion > 0:
    print("positive; one-digit")
elif -10 <= qustion < 0:
    print("negative; one-digit")
elif 10 <= qustion > 0:
    print("positive; two-digit")
elif -10 > qustion < 0:
    print("negative; two-digit")
else:
    print("Zero is neither positive nor negative number!")
