class Fish:
    """Fish. It has weight.
        Fish has two derived classes: SheatFish and Carp.
        SheatFish should have whisckerLength, Carp should have color.
        You can also add optional attributes (as you wish)."""

    def __init__(self, name, weight, feature=None):
        self.name = name
        self.weight = weight
        self.feature = feature


class SheatFish(Fish):

    def __init__(self, name, weight, feature):
        super().__init__(name, weight, feature)
        self.whisckerLenght = feature


class Carp(Fish):

    def __init__(self, name, weight, feature):
        super().__init__(name, weight, feature)
        self.color = feature
