import math
print('Введіть довжину двох катетів в сантиметрах')


a = int(input())
b = int(input())

hypotenuse = math.sqrt((pow(a,2) + pow(b,2)))

print('Гіпотенуза =', hypotenuse, 'см')