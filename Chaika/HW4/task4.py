# Task 4
# Is it possible to place a round stage with radius R in a square hall of square S so that there is a passage was at 
# least K from the wall to the stage?
# Задача 4
# Можно ли разместить круглую сцену радиусом R в квадратном зале квадрата S так, чтобы от стены до сцены проход был не менее K?

r = float(input('input radius R: '))
s = float(input('input hall area S: '))
k = float(input('input wall to the stage K: '))
ss = s ** 0.5

if ss - k - r >= 0:
    print("Vozmozhno razmestit' scenu radiusom ", "%.2f" % r,  ", v kvadrate ploshhad'ju ", "%.2f" % s, ", s rasstojaniem do steny ", "%.2f" % k )
else:
    print("Ne vozmozhno razmestit' scenu radiusom ", "%.2f" % r,  ", v kvadrate ploshhad'ju ", "%.2f" % s, ", s rasstojaniem do steny ", "%.2f" % k )