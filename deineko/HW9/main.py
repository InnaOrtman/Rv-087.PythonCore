from pond import *
from fishModels import*
from gameplay import *
import subprocess

start = int(input('Enter 1 to start the game: '))

while start == 1:
    print(printMenu())

    userChoice = int(input( ))

    if userChoice == 1:
        subprocess.call("cls", shell=True)
        print('You have', len(pond.capacity), 'fishes in your pond.')
        checkOrNot = int(input('Enter 1 to check your fishes, enter any other key to go back: '))
        if checkOrNot == 1:
            subprocess.call("cls", shell=True)
            pond.showAllTheFishes()

    elif userChoice == 2:
        subprocess.call("cls", shell=True)
        print('The pond is ', pond.showState())

    elif userChoice == 3:
        subprocess.call("cls", shell=True)
        pond.obtainRandomFish()
        print('You have added: ', pond.capacity[-1])

    elif userChoice == 4:
        subprocess.call("cls", shell=True)
        pond.showAllTheFishes()
        whichOne = int(input('This is a list of fishes in the pond, select which one of them do you want to catch? '))
        pond.catchTheFish(whichOne)

    elif userChoice == 5:
        subprocess.call("cls", shell=True)
        pond.showTheCatchedFishes()
        bringBack = int(input('There is a list of catched fishes which one do you want to bring back? '))
        pond.bringTheFishBack(bringBack)

    elif userChoice == 6:
        subprocess.call("cls", shell=True)
        yourOwnFish.name = str(input('Enter the name of your fish: '))
        yourOwnFish.weight = int(input('Enter a weight of your fish: '))
        yourOwnFish.ownAttributeName = str(input('Which attribute does your fish have? '))
        yourOwnFish.ownAttribute = input(f"Enter {yourOwnFish.ownAttributeName} of your fish: ")
        print(yourOwnFish)
        ownFishToPond = int(input('If you want to add this fish to your pond, press 1 '))
        if ownFishToPond == 1:
            pond.capacity.append(yourOwnFish)
            print('Congratulations! You have added ', yourOwnFish, 'to your pond.')

    elif userChoice == 7:
        subprocess.call("cls", shell=True)
        print('Goodbye!')
        break



