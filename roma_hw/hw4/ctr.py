import math

print("**********Choose an Option:********* ");
print("1: Area of the Circle");
print("2: Area of the Rectangle ");
print("3: Area of the Triangle ");

# input the geometry shape
choice = int(input(""))

# area of the circle
if choice==1:
    # input circle radius
    radius = float(input("Enter the radius of the Circle: "))
    area = math.pi*pow(radius,2)
    print(f"The area of the circle with radius {radius} is : {round(area,2)}")

#area of the rectangle
if choice==2:
    width =float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))
    area = width*length
    print(f"The area of the ractangle is {round(area,2)}")

# area of triangle using heron's formula
if choice ==3:
    a, b , c = map(float, input("Enter the 3 sides of triangle eg (12 13 14):").split())
    s= (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"The area of the triangle is {round(area,2)}")