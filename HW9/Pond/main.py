import os
from random import randint
from pond import *
from fisherman import *


def clear():
    return os.system('clear')


if __name__ =='__main__':

    lake = Pond()
    player = Fisherman()

    print("Type 1 to start game.")
    print("Type 2 to exit")
    x = int(input())
    if x == 1:
        lake = Pond()
    clear()

    while x == 1:
        print("\n")
        print("Type 1 to check pond status")
        print("Type 2 to add random fish to pond")
        print("Type 3 to catch random fish from pond")
        print("Type 4 to check your caught fish")
        print("Type 5 to release fish back")
        print("Type 6 to exit game")
        y = int(input())

        if y == 1:
            clear()
            lake.show_state()
            lake.show_capacity()
        elif y == 2:
            clear()
            lake.obtain_fish()
        elif y == 3:
            clear()
            player.catch_fish(lake)
        elif y == 4:
            clear()
            player.print_caught_fish_list()
        elif y == 5:
            clear()
            player.release_fish(lake)
        elif y == 6:
            x = 0
        stopper = 0
        while stopper != "":
            stopper = input("\npress enter to continue\n")
        clear()

