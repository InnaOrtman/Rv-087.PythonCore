import fishes
from random import randint

class Pond:
    def __init__(self):
        self.capacity = []
        self.state = "empty"

    def create_random_sheatfish(self):
        return fishes.SheatFish(randint(1, 10), randint(1, 10))

    def create_random_carp(self):
        colors = ("Red", "Blue", "Green", "Yellow", "Black", "White")
        x = len(colors) - 1

        return fishes.Carp(str(colors[randint(0, x)]), randint(0, 10))

    def check_pond_state(self):
        if len(self.capacity) < 1:
            self.state = "empty"
        elif len(self.capacity) < 5:
            self.state = "poor"
        elif 5 <= len(self.capacity) <= 10:
            self.state = "normal"
        elif len(self.capacity) > 10:
            self.state = "rich"

        return self.state

    def obtain_fish(self, *params):
        if len(params) > 0:
            for i in params:
                self.capacity.append(i)
        else:
            fish_count = int(input("Please type in the quantity of fish you want to add.\n"))

            while fish_count > 0:
                x = randint(1, 2)
                if x == 1:
                    self.capacity.append(self.create_random_sheatfish())
                else:
                    self.capacity.append(self.create_random_carp())
                fish_count -= 1

        self.check_pond_state()

    def lost_fish(self):
        if len(self.capacity) == 0:
            print("\nThere is no fish!")
            return
        x = self.capacity.pop(randint(0, (len(self.capacity) - 1)))
        self.check_pond_state()
        return x

    def show_capacity(self):
        print(f"Fish quantity: {len(self.capacity)}.\nList of fish:")
        for i in self.capacity:
            print(f"{self.capacity.index(i) + 1}: {i}")

    def show_state(self):
        print(f"State: {self.state}")