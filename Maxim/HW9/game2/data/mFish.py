class Fish:
    """Fish. It has weight.
        Fish has two derived classes: SheatFish and Carp.
        SheatFish should have whisckerLength, Carp should have color.
        You can also add optional attributes (as you wish)."""

    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value


class SheatFish(Fish):
    def __init__(self, name, weight, whisckerLenght):
        super().__init__(name, weight)
        self.__whisckerLenght = whisckerLenght

    @property
    def whisckerLenght(self):
        return self.__whisckerLenght

    @whisckerLenght.setter
    def whisckerLenght(self, whisckerLenght):
        self.__whisckerLenght = whisckerLenght


class Carp(Fish):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
