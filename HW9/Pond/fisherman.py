from pond import *

class Fisherman:
    fish_caught = 0
    caught_fish_list = []

    def catch_fish(self, place):
        if int(len(place.capacity)) <= 0:
            print("Sorry, there is no fish.")
            return
        else:
            print("Your try to catch a fish.")
            x = place.lost_fish()
            print(f"You caught {x}")
            Fisherman.caught_fish_list.append(x)

    def print_caught_fish_list(self):
        print(f"Number of caught fish: {len(self.caught_fish_list)}")
        for i in self.caught_fish_list:
            print(f"{self.caught_fish_list.index(i)+1}: {i}")

    def release_fish(self, place):


        print(f"List of fish you have:")
        if len(self.caught_fish_list) < 1:
            print(f"You have no fish to release")
            return

        for i in self.caught_fish_list:
            print(f"{self.caught_fish_list.index(i)+1}: {i}")
        x = -1
        while x < 0 or x > len(self.caught_fish_list):
            x = int(input("Please enter the number of fish to release\n"))

        place.obtain_fish(self.caught_fish_list.pop(x-1))