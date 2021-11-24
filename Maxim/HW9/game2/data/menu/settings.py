import csv
import os
import shutil

from .. import mFish
from ..msg import Msg as msg


class Settings:
    def __init__(self):
        self.__settings = True

    def getSettings(self):
        return self.__settings

    def setSettings(self, value):
        self.__settings = value

    settings = property(getSettings, setSettings)

    def endSettings(self):
        self.settings = False

    @staticmethod
    def createCarp(avalibleFishes):
        while True:
            choice = input(msg.msgCreateCarp)
            if choice == "q":
                return avalibleFishes
            choice = choice.lower().split()
            if len(choice) != 2:
                print(msg.incorrValue)
                continue
            fish = mFish.Carp("carp", choice[0], choice[1])
            avalibleFishes.append(fish)
            with open("data/avalible.csv", "a", newline="",
                      encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow([fish.name, fish.weight, fish.color])

    @staticmethod
    def createSheatfish(avalibleFishes):
        while True:
            choice = input(msg.msgCreateSheatfish)
            if choice == "q":
                return avalibleFishes
            choice = choice.lower().split()
            if len(choice) != 2:
                print(msg.incorrValue)
                continue
            fish = mFish.SheatFish("sheatfish", choice[0], choice[1])
            avalibleFishes.append(fish)
            with open("data/avalible.csv", "a", newline="",
                      encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow([fish.name, fish.weight, fish.whisckerLenght])

    @staticmethod
    def createComFish(avalibleFishes):
        while True:
            choice = input(msg.msgCreateCommFish)
            if choice == "q":
                return avalibleFishes
            choice = choice.lower().split()
            if len(choice) != 2:
                print(msg.incorrValue)
                continue
            fish = mFish.Fish(choice[0], choice[1])
            avalibleFishes.append(fish)
            with open("data/avalible.csv", "a", newline="",
                      encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow([fish.name, fish.weight])

    @staticmethod
    def watchAvalfishes(avalibleFishes):
        print("   Avalible fishes: ")
        lst = AvalibleFish.avalibleFishList(avalibleFishes)
        for i in range(len(lst)):
            print(f"   {i+1}) {lst[i][0]} {lst[i][1]}kg" if
                  len(lst[i]) == 2 else
                  f"   {i+1}) {lst[i][0]} {lst[i][1]}kg {lst[i][2]}")
        print()

    @staticmethod
    def delFish(avalibleFishes):
        while True:
            choice = input(msg.msgDelFish)
            if choice == "q":
                return avalibleFishes
            if 0 < int(choice) < len(avalibleFishes) + 1:
                del avalibleFishes[int(choice)-1]
                print("fish deleted")
                inp = open('data/avalible.csv', 'r')
                output = open('data/tmp.csv', 'w')
                writer = csv.writer(output)
                count = 1
                for row in csv.reader(inp):
                    if count != int(choice):
                        writer.writerow(row)
                    count += 1
                inp.close()
                output.close()
                os.remove("data/avalible.csv")
                os.rename('data/tmp.csv', 'data/avalible.csv')
            else:
                print(msg.incorrValue)


class AvalibleFish:
    @staticmethod
    def loadAvalFishListObj():
        avalibleFishes = []
        with open("data/avalible.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if row[0] == "carp".lower():
                    avalibleFishes.append(mFish.Carp(row[0], row[1], row[2]))
                    continue
                if row[0] == "sheatfish".lower():
                    avalibleFishes.append(mFish.SheatFish(
                        row[0], row[1], row[2]))
                    continue
                else:
                    avalibleFishes.append(mFish.Fish(row[0], row[1]))
            return avalibleFishes

    @staticmethod
    def avalibleFishList(avalibleFishes):
        res = []
        for i in range(len(avalibleFishes)):
            if avalibleFishes[i].name == "carp":
                tmp = [avalibleFishes[i].name,
                       avalibleFishes[i].weight,
                       avalibleFishes[i].color]
                res.append(tmp)
            elif avalibleFishes[i].name == "sheatfish":
                tmp = [avalibleFishes[i].name,
                       avalibleFishes[i].weight,
                       avalibleFishes[i].whisckerLenght]
                res.append(tmp)
            else:
                tmp = [avalibleFishes[i].name,
                       avalibleFishes[i].weight]
                res.append(tmp)
        return res

    @staticmethod
    def loadAvalFishListPondObj():
        shutil.copyfile("data/save.csv", "data/tmp.csv")
        f = open("data/save.csv", "w")
        f.truncate()
        f.close()
        loadFishPondObj = []
        with open("data/tmp.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if row[0] == "carp".lower():
                    loadFishPondObj.append(mFish.Carp(row[0], row[1], row[2]))
                    continue
                if row[0] == "sheatfish".lower():
                    loadFishPondObj.append(mFish.SheatFish(
                        row[0], row[1], row[2]))
                    continue
                else:
                    loadFishPondObj.append(mFish.Fish(row[0], row[1]))
        return loadFishPondObj
