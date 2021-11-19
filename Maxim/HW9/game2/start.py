# carp bream perch pike pikeperch roach redeye crucian_carp sheatfish

from data.menu import mainMenu
import data.msg as msg


menu = mainMenu.Menu()
while menu.mainMenu:
    print(msg.Msg.mainMenu)
    choice = input(menu.entYoCho)
    if choice == "1":
        menu.newGame()
        firstRun = False
        continue
    if choice == "2":
        menu.loadGame()
        continue
    if choice == "3":
        menu.settings()
        continue
    if choice == "0":
        menu.end()
        continue
    else:
        print(msg.Msg.incorrValue)
