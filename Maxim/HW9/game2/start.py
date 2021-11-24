# carp bream perch pike pikeperch roach redeye crucian_carp sheatfish
try:
    import data.msg as msg
    from data.menu import mainMenu
except ImportError:
    print("The integrity of the game is violated!\n"
          "Please, reinstall the game")
else:
    try:
        menu = mainMenu.Menu()
    except AttributeError:
        print(f"\n{msg.Msg.endGame}")
    except Exception:
        print("Unknown error")
    else:
        while menu.mainMenu:
            print(msg.Msg.mainMenu)
            try:
                choice = input(menu.entYoCho)
            except (KeyboardInterrupt, EOFError):
                print(f"\n{msg.Msg.endGame}")
                break
            else:
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
