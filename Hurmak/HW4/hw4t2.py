shape = input('Enter shape type (rectangle, triangle, circle): ')
if shape == 'rectangle':
    side1 = float(input('Enter side 1 of rectangle:'))
    side2 = float(input('Enter side 2 of rectangle:'))
    area = side1 * side2
elif shape == 'triangle':
    side1 = float(input('Enter side 1 of triangle:'))
    side2 = float(input('Enter side 2 of triangle:'))
    area = side1 * side2 / 2
elif shape == 'circle':
    radius = float(input('Enter radius:'))
    area = 3.1415 * radius ** 2
else:
    area = False

print(f'Area of {shape} is equal to {area}' if area else 'wrong shape entered ')
