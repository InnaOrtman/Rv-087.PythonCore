from math import hypot
choice = int(input("Please input 1 for rectangle, 2 for triangle, 3 for circle.\n"))

if choice < 1 or choice > 3:
    choice = input("Please input 1-3 only.\n")
    
if choice == 1:
    a = int(input("Please input side a.\n"))
    b = int(input("Please input side b.\n"))
    area = a*b
    print(f"The area of rectangle with side a = {a}, b = {b} is {area}")
elif choice == 2:
    a = int(input("Please input side a.\n"))
    b = int(input("Please input side b.\n"))
    c = int(input("Please input side c.\n"))
    semi_perimeter = (a+b+c) / 2    
    area = (semi_perimeter*(semi_perimeter-a)*(semi_perimeter-b)*(semi_perimeter-c)) ** 0.5
    print(f"The area of triangle with side a = {a}, b = {b}, c = {c} is {area}")
else:
    radius = int(input("Please input radius.\n"))
    PI = 3.1415
    area = PI * (radius**2)
    print(f"The area of circle with radius {radius} is {area}")