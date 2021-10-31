# Task 6*
# The number of a place in the reserved carriage is given. Determine which place it is: top or bottom, compartment or side
# Задание 6 *
# Приведен номер места в забронированном вагоне. Определите, в каком месте он находится: сверху или снизу, в отсеке или сбоку.
# СХЕМА ВАГОНА
# https://www.biletik.aero/handbook/blog/poezda/platskartnye-vagony-rzhd-numeratsiya-mest-v-vagone-skhema-raspolozheniya-luchshie-mesta-foto/

num = int(input('Vvedi Vashe mesto v diapazone ot 1 do 54: '))
numh = num % 2

if num <= 36:
    if numh == 0:
        print('Vashe mesto ', num, ' nahoditsya v otseke sverhu') 
    else:
        print('Vashe mesto ', num, ' nahoditsya v otseke vnizu') 
elif 54 >= num > 36:
    if numh == 0:
        print('Vashe mesto ', num, ' nahoditsya sboku sverhu') 
    else:
        print('Vashe mesto ', num, ' nahoditsya sboku vnizu') 
else:
    print('Vy vveli ne sushchestvuyushchee mesto nomer - ', num,  '\nVvedi Vashe mesto v diapazone ot 1 do 54')