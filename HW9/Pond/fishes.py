from random import randint

class Fish:
    weight = 1


class SheatFish(Fish):
    whisker_length = 0

    def __init__(self, whisker_length=1, weight=1):
        self.whisker_length = whisker_length
        self.weight = weight


    def __str__(self):
        return f"Sheatfish, weight: {self.weight}, whisker length: \
{self.whisker_length}."


class Carp(Fish):
    color = "green"

    def __init__(self, color="green", weight=1):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"Carp, weight: {self.weight}, color: {self.color}"

