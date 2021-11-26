from random import randint
from fishModels import *


class Pond:
    def __init__(self):
        self.capacity = []
        self.catchedFishes = []
        self.state = ''

    def showState(self):
        if len(self.capacity) < 1:
            self.state = 'empty'
        elif len(self.capacity) < 5:
            self.state = 'poor'
        elif len(self.capacity) < 10:
            self.state = 'normal'
        elif len(self.capacity) >= 10:
            self.state = 'rich'

        return self.state

    def obtainRandomFish(self):
        whichFish = randint(1,2)

        if whichFish == 1:
            self.capacity.append(SheatFish(randint(1,100), randint(1,20)))
        else:
            whichColor = randint(1,3)
            if whichColor == 1:
                self.capacity.append(Carp(randint(1,5), 'Blue'))
            elif whichColor == 2:
                self.capacity.append(Carp(randint(1,5), 'Golden'))
            else:
                self.capacity.append(Carp(randint(1,5), 'Red'))

    def showAllTheFishes(self):
        for i in range(len(self.capacity)):
                print(i+1,' - ', self.capacity[i])

    def catchTheFish(self, whichOne):
        if len(self.capacity) > 0:
            whichOne -= 1
            if self.capacity[whichOne].weight < 30:
                
                self.catchedFishes.append(self.capacity[whichOne])
                self.capacity.pop(whichOne)
                print('Congratulations: you have catched ', self.catchedFishes[-1])
            else:
                print('Your fishing rod is too weak. To catch the fish with weight more \
than 30 kg you need to buy a new one: 4441 1144 2038 2028')

        else: print('You do not have fishes i your pond, please add them!')

    def showTheCatchedFishes(self):
        for i in range(len(self.catchedFishes)):
            print(i+1, ' - ', self.catchedFishes[i])

    def bringTheFishBack(self, bringBack):
        bringBack -= 1
        self.capacity.append(self.catchedFishes[bringBack])
        self.catchedFishes.pop(bringBack)
        print('You have brought ', self.capacity[-1], 'back')
