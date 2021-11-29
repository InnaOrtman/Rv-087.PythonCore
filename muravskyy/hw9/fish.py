class Fish:
    def __init__(self, weight):
        self.weight = weight
       
    def checkValue(x):
        if isinstance(x, float) \
            or isinstance(x, int):
            return True
        return False

class Carp(Fish):
    def __init__(self, color, weight):
        super().__init__(weight)
        self.color = color    

class SheatFish(Fish):
    def __init__(self, whisckerlenght, weight):
        super().__init__(weight)
        self.whisckerlenght = whisckerlenght