# User should have interactive menu:
# 1. View capacity;
# 2. View state of Pond;
# 3. Add fish( Carp or SheatFish);
# 4. Catch fish (concrete instance);
# 5. Create new fish (fill himself the creator)))
# 6. Finish the game.

import mPond
import mFish


posibleFish = ("carp", "bream", "perch",
               "pike", "pikeperch", "roach",
               "redeye", "crucian_carp", "sheatfish")
incorData = "You entered incorect data\n"
pond = mPond.Pond()
quit_ = False
while not quit_:
    print("1. View capacity\n"
          "2. View state of Pond\n"
          "3. Add fish(Carp or SheatFish or other)\n"
          "4. Catch fish (concrete instance)\n"
          "5. Finish the game\n")

    choice = int(input("Eneter you choice: "))
    if choice == 1:
        print(pond.showCapacity(), "\n")
        continue
    if choice == 2:
        print(pond.showState(), "\n")
        continue
    if choice == 3:
        fish = input("Enter what the fish you want to add: ").lower().split()
        if len(fish) > 3:
            print(incorData)
            continue
        if fish[0] not in posibleFish:
            print("You can't add such kind of fish\n")
            continue
        if fish[0] == "carp":
            fishObj = mFish.Carp(*fish)
            pond.obtainFish(fishObj)
            continue
        if fish[0] == "sheatfish":
            fishObj = mFish.SheatFish(*fish)
            pond.obtainFish(fishObj)
            continue
        fishObj = mFish.Fish(*fish)
        pond.obtainFish(fishObj)
    if choice == 4:
        fish = input("Enter what fish you catched: ").lower()
        if fish in posibleFish:
            catch = pond.lostFish(fish)
            if not catch:
                print("There is no such fish in the pond\n")
            else:
                print(f"You catch the fish "
                      f"{catch.name, catch.weight, catch.feature}")

        else:
            print(incorData)
            continue
    if choice == 5:
        quit_ = True
