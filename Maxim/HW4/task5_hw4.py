# Task 5
# The amount of money is known.
# Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible
# TODO: make a better output

import parrPathApp
from mynum import is_positive_integer
from mynum import if_int_to_int


parrPathApp.run()


def main():
    balBanknotes = {"200": 0,
                    "100": 0,
                    "10": 0,
                    "1": 0}

    money = input("Enter amount of money: ")
    if not is_positive_integer(money):
        print("You entered not a value of money or "
              "not integer amount of money")
        return -1

    money = float(money)

    for item in balBanknotes.items():
        moneyDiv = money // float(item[0])

        if moneyDiv != 0:
            balBanknotes[item[0]] = if_int_to_int(moneyDiv)

        money = int(money) - int(moneyDiv) * int(item[0])

    print(balBanknotes)


if __name__ == "__main__":
    main()
