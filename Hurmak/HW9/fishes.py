class Fish:
    instances: set
    instances = set()

    def __init__(self, weight):
        self.weight = weight
        Fish.instances.add(self)

    def __repr__(self):
        return f'| Weight: {self.weight}'


class Carp(Fish):

    def __init__(self, weight, color):
        super().__init__(weight)
        self.color = color

    def __repr__(self):
        return f'Carp ' + super().__repr__() + f' | {self.color}'


class Sheatfish(Fish):

    def __init__(self, weight, whisckerLength):
        super().__init__(weight)
        self.whisckerLength = whisckerLength

    def __repr__(self):
        return f'Sheatfish ' + super().__repr__() + f" | Whisker= {self.whisckerLength}"
