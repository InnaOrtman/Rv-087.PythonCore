# task_2
import math

choice = int(input("Calculate the square of either a rectangle (1), or a triangle(2), or a circle(3)\nEnter the number: "))

if choice == 1:
    height = int(input("Enter the height of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    S = height * width
    print(f"The area of the rectangle is: {S}")
elif choice == 2:
    height = int(input("Enter the height of the triangle: "))
    side = int(input("Enter the side of the triangle: "))
    print(f"The area of the triangle  is : {0.5*height*side}")
elif choice == 3:
    radius = int(input("Enter the radius : "))
    print(f"The square of circle is: {round(math.pi * (radius ** 2))}")
else:
    print("Enter the correct number, please!")



