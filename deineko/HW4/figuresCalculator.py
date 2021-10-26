import math


print("Select the figure, which area you want to calculate: 1 - Rectangle, 2 - Triangle, 3 - Circle")
choice = int(input()) 

if choice == 1:
    print("Enter rectangle\'s width")
    width = int(input())
    print('Enter rectangle\'s height')
    height = int(input())
    print('Rectangle\'s area =', width*height,'sm^2')
elif choice == 2:
    print("Enter first side")
    side1 = int(input())
    print("Enter second side")
    side2 = int(input())
    print("Enter third side")
    side3 = int(input())
    s = (side1+side2+side3)/2
    print('triangle\'s area = ', (s*(s-side1)*(s-side2)*(s-side3))**(1/2),'sm^2')
elif choice == 3:
    print('Enter circle\'s radius')
    radius = int(input())
    print("Circle\'s radius = ", math.pi*(radius**2), 'sm^2')

else: 
    print('Restart the programm and choose value between 1 and 3')