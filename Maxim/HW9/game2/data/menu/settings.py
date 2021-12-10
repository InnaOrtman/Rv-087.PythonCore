import csv
import os
import shutil
import string
from string import ascii_letters

try:
    from ..msg import Msg as msg
    from .. import mFish
    from mynum import is_number
    from ..err import MyErr
except ImportError:
    print("The integrity of the game is violated!\n"
          "Please, reinstall the game")
else:
    msgs = msg()


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
                try:
                    choice = input(msg.msgCreateCarp)
                except (KeyboardInterrupt, EOFError):
                    print(f"\n{msgs.endGame}")
                    exit(0)

                if choice == "q":
                    return avalibleFishes
                choice = choice.lower().split()
                if len(choice) != 2:
                    print(msg.incorrValue)
                    continue
                try:
                    if not is_number(choice[0]):
                        raise MyErr(msgs.notFNum)
                except MyErr:
                    print(msgs.notFNum)
                    continue
                try:
                    for i in choice[1]:
                        if i not in string.ascii_letters:
                            raise MyErr(msgs.notAlphab)
                except MyErr:
                    err = MyErr(msgs.notAlphab)
                    print(err)
                    continue
                else:
                    print("Carp is created")

                fish = mFish.Carp("carp", choice[0], choice[1])
                avalibleFishes.append(fish)
                with open("data/avalible.csv", "a", newline="",
                          encoding="utf-8") as f:
                    writer = csv.writer(f, delimiter=";")
                    writer.writerow([fish.name, fish.weight, fish.color])

        @staticmethod
        def createSheatfish(avalibleFishes):
            while True:
                try:
                    choice = input(msg.msgCreateSheatfish)
                except (KeyboardInterrupt, EOFError):
                    print(f"\n{msgs.endGame}")
                    exit(0)

                if choice == "q":
                    return avalibleFishes
                choice = choice.lower().split()
                if len(choice) != 2:
                    print(msg.incorrValue)
                    continue
                try:
                    if not is_number(choice[0]):
                        raise MyErr(msgs.notFNum)
                except MyErr:
                    err = MyErr(msgs.notFNum)
                    print(err)
                    continue
                try:
                    if not is_number(choice[1]):
                        raise MyErr(msgs.notSNum)
                except MyErr:
                    err = MyErr(msgs.notSNum)
                    print(err)
                    continue
                else:
                    print("Sheatfish is created")

                fish = mFish.SheatFish("sheatfish", choice[0], choice[1])
                avalibleFishes.append(fish)
                with open("data/avalible.csv", "a", newline="",
                          encoding="utf-8") as f:
                    writer = csv.writer(f, delimiter=";")
                    writer.writerow([fish.name, fish.weight, fish.whisckerLenght])

        @staticmethod
        def createComFish(avalibleFishes):
            while True:
                try:
                    choice = input(msg.msgCreateCommFish)
                except (KeyboardInterrupt, EOFError):
                    print(f"\n{msgs.endGame}")
                    exit(0)

                if choice == "q":
                    return avalibleFishes
                choice = choice.lower().split()
                if len(choice) != 2:
                    print(msg.incorrValue)
                    continue
                try:
                    for i in choice[0]:
                        if i not in string.ascii_letters:
                            raise MyErr(msgs.notAlphabF)
                except MyErr:
                    err = MyErr(msgs.notAlphabF)
                    print(err)
                    continue
                try:
                    if not is_number(choice[1]):
                        raise MyErr(msgs.notSNum)
                except MyErr:
                    err = MyErr(msgs.notSNum)
                    print(err)
                    continue
                else:
                    print("Fish is created")

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
                try:
                    choice = int(choice)
                except ValueError:
                    print("You entered not a number")
                    continue
                if 0 < int(choice) < len(avalibleFishes) + 1:
                    try:
                        inp = open('data/avalible.csv', 'r')
                    except FileNotFoundError:
                        print("Can't to delete the fish, Integr")
                        exit(0)
                    else:
                        try:
                            output = open('data/tmp.csv', 'w')
                        except PermissionError:
                            print(msgs.directPermiss)
                            print(msgs.endGame)
                            exit(0)
                        else:
                            writer = csv.writer(output)
                            count = 1
                            for row in csv.reader(inp):
                                if count != int(choice):
                                    writer.writerow(row)
                                count += 1
                            output.close()
                        finally:
                            inp.close()
                    try:
                        os.remove("data/avalible.csv")
                        os.rename('data/tmp.csv', 'data/avalible.csv')
                    except IOError:
                        print(msgs.directPermiss)
                        print(msgs.endGame)
                        exit(0)
                    del avalibleFishes[int(choice)-1]
                    print("fish deleted")
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
