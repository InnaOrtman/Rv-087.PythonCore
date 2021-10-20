print('Введіть висоту і ширину прямокутника в сантиметрах')

height = int(input())
width = int(input())

perimeter = 2*(height+width)
area = height*width

print('Периметр прямокутника = ', perimeter, 'см')
print('Площа прямокутника = ', area, 'см^2')