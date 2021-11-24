import random
import csv
import os


class Pond:
    """Pond. It should have the next attributes: capacity –
    list that contains all fish from the Pond in the current moment;
    state – ‘poor’, ‘normal’, ‘rich’. Pond is ‘poor’ if it’s capacity
    contains less then 5 fishes, ‘normal’, if capacity contains
    from 5 to 10 fishes, and ‘rich’ if it has more than 10 fishes.
    Pond can obtainFish() – it will be added to it’s capacity,
    and lostFish() – it will be taken from capacity. The Pond state
    changes automatically when it’s capacity reaches the appropriate
    value. Pond also allows showPapacity() and showState(). You can
    also add the optional attributes (as you wish)."""

    empt = "The pond is empty"

    def __init__(self):
        self.__capacity = []
        self.__state = self.empt

    def getState(self):
        return self.__state

    def setState(self, value):
        self.__state = value

    def getCapacity(self):
        return self.__capacity

    def setCapacity(self, value):
        self.__capacity = value

    state = property(getState, setState)
    capacity = property(getCapacity, setCapacity)

    def showCapacity(self):
        lst = []
        for i in range(len(self.capacity)):
            if self.capacity[i].feature is None:
                lst.append(f"{self.capacity[i].name} weight: "
                           f"{self.capacity[i].weight}")
            else:
                lst.append(f"{self.capacity[i].name} weight: "
                           f"{self.capacity[i].weight} "
                           f"{self.capacity[i].feature}")
        return lst

    def showState(self):
        return self.state

    def chageState(self):
        lenCapacity = len(self.capacity)
        if lenCapacity:
            if lenCapacity < 5:
                self.state = "poor"
            elif 4 < lenCapacity < 11:
                self.state = "normal"
            else:
                self.state = "rich"
        else:
            self.state = self.empt

    def obtainFish(self, obj):
        self.capacity.append(obj)
        if obj.name == "carp":
            lst = [obj.name, obj.weight, obj.color]
        elif obj.name == "sheatfish":
            lst = [obj.name, obj.weight, obj.whisckerLenght]
        else:
            lst = [obj.name, obj.weight]
        with open("data/save.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([*lst])
        self.chageState()
        print(f"fish added {lst}")

    def lostFish(self):
        lenCap = len(self.capacity)
        randFish = random.randint(1, lenCap)
        if randFish % 2 == 0:
            lst = []
            if self.capacity[randFish - 1].name == "carp":
                lst.append(self.capacity[randFish - 1].name)
                lst.append(self.capacity[randFish - 1].weight)
                lst.append(self.capacity[randFish - 1].color)
            elif self.capacity[randFish - 1].name == "sheatfish":
                lst.append(self.capacity[randFish - 1].name)
                lst.append(self.capacity[randFish - 1].weight)
                lst.append(self.capacity[randFish - 1].whisckerLenght)
            else:
                lst.append(self.capacity[randFish - 1].name)
                lst.append(self.capacity[randFish - 1].weight)
            print(f"Congratulation! You catch ", end="")
            print(f"{lst[0]} {lst[1]} kg" if len(lst) == 2 else
                  f"{lst[0]} {lst[1]} kg {lst[2]}")

            del self.capacity[randFish - 1]
            self.chageState()
            inp = open('data/save.csv', 'r')
            output = open('data/tmp.csv', 'w')
            writer = csv.writer(output)
            count = 1
            for row in csv.reader(inp):
                if count != int(randFish):
                    writer.writerow(row)
                count += 1
            inp.close()
            output.close()
            os.remove("data/save.csv")
            os.rename('data/tmp.csv', 'data/save.csv')
        else:
            print("Failed to catch fish. Try again...")

    def avalibleFishListPond(self):
        res = []
        for i in range(len(self.capacity)):
            if self.capacity[i].name == "carp":
                tmp = [self.capacity[i].name,
                       self.capacity[i].weight,
                       self.capacity[i].color]
                res.append(tmp)
            elif self.capacity[i].name == "sheatfish":
                tmp = [self.capacity[i].name,
                       self.capacity[i].weight,
                       self.capacity[i].whisckerLenght]
                res.append(tmp)
            else:
                tmp = [self.capacity[i].name,
                       self.capacity[i].weight]
                res.append(tmp)
        return res

    def newGame(self):
        self.capacity = []
        self.state = self.empt
