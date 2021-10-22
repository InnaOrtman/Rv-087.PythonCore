# task_5
from math import sqrt

leg_1 = int(input("Enter the length of the leg of the triangle №1: "))
leg_2 = int(input("Enter the length of the leg of the triangle №2: "))

hypotenuse = sqrt(leg_1**2 + leg_2**2)

print(f"The length of the hypotenuse is:{round((hypotenuse),2)}")


