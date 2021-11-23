from task_1 import Pond, Carp, Fish, SheatFish

"""
Щось поки трохи сумбурно вийшло:), 
але ще планую вдосконалювати...
"""

pond = Pond()
fish = Fish()
print("🙃🙃🙃HELLO🙃🙃🙃\nWelcome to the Fishing Game!\nWe \
we have a pond with only 1 fish here!")

game_is_on = True
while game_is_on:
    q = input("!!Enter the numbers according to the steps you want to perform!!\n1. View capacity;\n2. View state of Pond;\n3. Add fish( Carp or SheatFish);\n4. Catch fish (concrete instance);\n5. Create new fish (fill himself the creator)))\n6. Finish the game\n!!!Enter here - ")
    if q == '1':
        pond.showCapacity()
    elif q == '2':
        pond.showState()
    elif q == '3':
        pond.obtainFish()
    elif q == '4':
        pond.lostFish()
    elif q == '5':
        i = input("Enter !1! if you want to create carp to the pond and !2! if SheatFish\n!!!Enter here - ")
        if i == '1':
            n = int(input("Enter the color of the carp - yellow(1) or gold(2)\n!!!Enter here - "))
            if n == 1:
                n = "yellow"
                carp = Carp(n)
                carp.addCarp()
                carp.counterWeight()
            elif n == 2:
                n = "gold"
                carp = Carp(n)
                carp.addCarp()
                carp.counterWeight()
            else:
                print("Incorrect data...")
                break
        elif i == '2':
            n = int(input("Enter enter the length (from 0 to 12) of the SheatFish mustache\n!!!Enter here - "))
            sheatfish = SheatFish(n)
            sheatfish.addSheatFish()
            sheatfish.counterWeight()
        else:
            print("Incorrect data...")
            break
        s = int(input(f"Enter !1! if you want to add yor fish to the pond and !2! if not!\n!!!Enter here - "))
        if s == 1:
            pond.obtainFish()
        if s == 2:
            continue
    elif q == '6':
        game_is_on = False
        pond.showCapacity()
        pond.showState()
        print("😭😭!!GOODBYE!!😭😭")
        break
    else:
        print("Incorrect data...")
