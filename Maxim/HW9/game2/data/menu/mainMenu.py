from . import game
from . import settings
from ..msg import Msg as msg
from .settings import AvalibleFish
from .game import pond


startGame = game.Game()
settings = settings.Settings()
avalibleFishes = AvalibleFish().loadAvalFishListObj()


class Menu(msg):
    def __init__(self):
        self.__mainMenu = True
        self.__firstRun = True

    @property
    def mainMenu(self):
        return self.__mainMenu

    @mainMenu.setter
    def mainMenu(self, value):
        self.__mainMenu = value

    @property
    def firstRun(self):
        return self.__firstRun

    @firstRun.setter
    def firstRun(self, value):
        self.__firstRun = value

    @staticmethod
    def game():
        startGame.startMenu = True
        print(msg.game)
        while startGame.startMenu:
            choice = input(msg.entYoCho)
            if choice == "1":
                startGame.catchFish()
                continue
            if choice == "2":
                startGame.watchStatus()
                continue
            if choice == "3":
                startGame.watchAvalFishPond()
                continue
            if choice == "4":
                startGame.addFishPond(avalibleFishes)
                continue
            if choice == "0":
                startGame.endGame()
            else:
                print(msg.incorrValue)

    def newGame(self):
        f = open("data/save.csv", "w")
        f.truncate()
        f.close()
        pond.newGame()
        self.firstRun = False
        self.game()

    def loadGame(self):
        if self.firstRun:
            lstObj = AvalibleFish.loadAvalFishListPondObj()
            for i in range(len(lstObj)):
                pond.obtainFish(lstObj[i])
        self.firstRun = False
        self.game()

    def end(self):
        print(msg.endGame)
        self.mainMenu = False

    @staticmethod
    def settings():
        print(msg.settigsMenu)
        settings.settings = True
        while settings.settings:
            choice = input(msg.entYoCho)
            print()
            if choice == "1":
                settings.createCarp(avalibleFishes)
                continue
            if choice == "2":
                settings.createSheatfish(avalibleFishes)
                continue
            if choice == "3":
                settings.createComFish(avalibleFishes)
                continue
            if choice == "4":
                settings.watchAvalfishes(avalibleFishes)
                continue
            if choice == "5":
                settings.delFish(avalibleFishes)
                continue
            if choice == "0":
                settings.endSettings()
                continue
            else:
                print(msg.incorrValue)
