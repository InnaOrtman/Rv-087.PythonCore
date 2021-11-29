from fish import *
from pond import *
from menu import *


list_carp_color = [ 'black', 'white', \
     'red', 'pink', 'orange', 'yellow']
pond = Pond()
carp = Carp('black', 10)
sheatfish = SheatFish(2.3 ,30)
pond.obtainFish('carp', carp.__dict__)
pond.obtainFish('sheatfish',\
         sheatfish.__dict__)
count_fish = 1
while True:
    enter = int(input(Menu.gameMenu))
    if enter == 1:
        pond.showCapacity()
        Menu.msgReturn()
        continue
    elif enter == 2:
        pond.showState()
        Menu.msgReturn()
    elif enter == 3:
        fish = int(input(Menu.msgAddFish))
        if fish == 1:
            print(*list_carp_color)
            color = input(Menu.msgColor).lower
            weight = float(input(Menu.msgWeight))
            carp2 = Carp(color, weight)
            count_fish += 1
            name_fish = 'carp' + str(count_fish)
            pond.obtainFish(name_fish, carp2.__dict__)
            print('check state of pond')
            Menu.msgReturn('check capacity of the pond')
        if fish == 2:
            lenght = float(input(Menu.msglenght))
            weight = float(input(Menu.msgWeight))
            sheatfish2 = SheatFish(lenght, weight)
            count_fish += 1
            name_fish = 'sheatFish' + str(count_fish)
            pond.obtainFish(name_fish, sheatfish2.__dict__)
            Menu.msgReturn('check capacity of the pond')
        else:
            Menu.msgReturn('check only 1 or 2')
            continue
    elif enter == 4:
        print('\n', *[x for x in pond.capacity.keys()])
        lost_fish = input(Menu.msgLostFish).lower()
        if lost_fish in pond.capacity.keys():
            pond.lostFish(lost_fish)
            Menu.msgReturn('check capacity of the pond')
        else:
            Menu.msgReturn('incorrect name')
    elif enter == 0:
        break