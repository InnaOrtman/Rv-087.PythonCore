class Fish:
    weight = 5

class SheatFish(Fish):
    def __init__(self, weight = 5, whiskerLength = 10):
        self.weight = weight
        self.whiskerLength = whiskerLength

    def __str__(self):
        return f"Sheatfish. Weight: {self.weight} kg, whisker length: {self.whiskerLength}."
    

class Carp(Fish):
    def __init__(self, weight = 5, color = 'Blue'):
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"Carp. Weight: {self.weight} kg, Color: {self.color}."

class OwnFish(Fish):
    def __init__(self, name = 'Salmon', weight = 10, ownAttributeName = 'Age', ownAttribute = 3):
        self.name = name
        self.weight = weight
        self.ownAttributeName = ownAttributeName
        self.ownAttribute = ownAttribute

    def __str__(self):
        return f"{self.name}. Weight: {self.weight} kg, {self.ownAttributeName}: {self.ownAttribute}"
