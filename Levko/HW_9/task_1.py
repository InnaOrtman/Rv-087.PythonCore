# task_1
"""
Щось поки трохи сумбурно вийшло:),
але ще планую вдосконалювати...
"""


class Pond(object):

    def __init__(self):
        self.capacity = 1
        self.state = ""

    def obtainFish(self):
        self.capacity += 1
        print("🙃🙃🙃You launched a fish into a pond🙃🙃🙃")

    def lostFish(self):
        self.capacity -= 1
        print ( "🙃🙃🙃You caught a fish from the pond🙃🙃🙃" )

    def showCapacity(self):
        print(f'🙃🙃🙃The capacity of pond contains from {(self.capacity)} fish🙃🙃🙃')

    def showState(self):
        if self.capacity <= 5:
            self.state = '!poor!'
        if self.capacity > 5:
            self.state = '!normal!'
        if self.capacity > 10:
            self.state = '!rich!'
        print(f"🙃🙃🙃The Pond is - {self.state}🙃🙃🙃")


class Fish(object):

    def __init__(self):
        self.weight = 0
        self.dict = {}

    def counterWeight(self):
        print(f"🙃🙃🙃The weight of your FISH in the pond will be {self.weight}!🙃🙃🙃")


class SheatFish(Fish):

    def __init__(self, whisckerLength):
        super().__init__()
        self.whisckerLength = whisckerLength

    def addSheatFish(self):
        if self.whisckerLength > 6:
            self.weight = 50
        else:
            self.weight = 100


class Carp(Fish):

    def __init__(self, color):
        super().__init__()
        self.color = color

    def addCarp(self):
        if self.color == "yellow":
            self.weight = 25
        elif self.color == "gold":
            self.weight = 12


