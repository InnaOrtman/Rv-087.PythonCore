import math
print('Введіть радіус кола в сантиметрах')
circleRadius = int(input())

perimeter = 2 * math.pi * circleRadius
area = math.pi * pow(circleRadius, 2)

print ('Периметр кола = ', perimeter, 'см')
print ('Площа кола = ', area, 'см^2')
