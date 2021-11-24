from .settings import Settings
from ..mPond import Pond
from ..msg import Msg as msg

pond = Pond()


class Game:
    def __init__(self):
        self.__startMenu = True

    def getStartMenu(self):
        return self.__startMenu

    def setStartMenu(self, value):
        self.__startMenu = value

    startMenu = property(getStartMenu, setStartMenu)

    @staticmethod
    def catchFish():
        if pond.capacity:
            pond.lostFish()
        else:
            print(pond.showState())

    @staticmethod
    def watchStatus():
        print(pond.showState())

    @staticmethod
    def watchAvalFishPond():
        fishPond = pond.avalibleFishListPond()
        if fishPond:
            for i in range(len(fishPond)):
                print(f"   {i+1}) {fishPond[i][0]} {fishPond[i][1]}kg" if
                      len(fishPond[i]) == 2 else
                      f"   {i+1}) {fishPond[i][0]} {fishPond[i][1]}kg "
                      f"{fishPond[i][2]}")
        else:
            print(pond.empt)

    @staticmethod
    def addFishPond(avalibleFishes):
        print()
        Settings.watchAvalfishes(avalibleFishes)
        while True:
            choice = input(msg.msgAddFishPond)
            if choice == "q":
                return
            if 0 < int(choice) < len(avalibleFishes) + 1:
                pond.obtainFish(avalibleFishes[int(choice)-1])
            else:
                print(msg.incorrValue)

    def endGame(self):
        self.startMenu = False
