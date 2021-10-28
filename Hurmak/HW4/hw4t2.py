shape = input('Enter shape type (rectangle, triangle, circle): ')
if shape == 'rectangle':
    side1 = float(input('Enter side 1 of rectangle:'))
    side2 = float(input('Enter side 2 of rectangle:'))
    area = side1 * side2
elif shape == 'triangle':
    side1 = float(input('Enter side 1 of triangle:'))
    side2 = float(input('Enter side 2 of triangle:'))
    side3 = float(input('Enter side 3 of triangle:'))
    p = (side1 + side2 + side3)/2
    area = (p*(p - side1)*(p - side2)*(p - side3))**1/2
elif shape == 'circle':
    radius = float(input('Enter radius:'))
    area = 3.1415 * radius ** 2
else:
    area = False
print(f'Area of {shape} is equal to {area}' if area else 'wrong shape entered ')
