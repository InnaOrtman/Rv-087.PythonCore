# Task 2
# Depending on the user's choice, calculate the square of ​​either a rectangle, or a triangle, or a circle. If a rectangle or triangle is selected, the lengths of the sides should be invited; is circle, its radius.
# В зависимости от выбора пользователя вычислите квадрат прямоугольника, треугольника или круга. 
# Если выбран прямоугольник или треугольник, следует указать длины сторон; круг, его радиус.

choice = int(input('''choose a shape:
1 - rectangle
2 - triangle
3 - circle
'''))

print(choice)
if choice == 1:
    a = float(input('input side A: '))
    b = float(input('input side B: '))
    print('square of the rectangle equal ', a*b )

elif choice == 2:
    a = float(input('input the hypotenuse of the triangle A: '))
    h = float(input('input the height of the triangle H: '))
    #c = float(input('input side C: '))
    print('square of the triangle equal ', 0.5*a*h )

elif choice == 3:
    r = float(input('input radius circle: '))
    print('square of the circle equal ', "%.2f" % (3.141592*(r**2)))