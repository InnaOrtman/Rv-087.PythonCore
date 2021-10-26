# Task 3
# The user enters a number, the program must display its description.
# For example, "positive one-digit", "negative two-digit", etc.

import parrPathApp
from mynum import is_number
from mynum import is_positive_number
from mynum import is_fraction_in_number


parrPathApp.run()


def run() -> [-1, dict]:
    userNumber = input("Enter a number: ")

    if not is_number(userNumber):
        return -1

    posOrNeg: str
    fract: str
    digits = 0

    if is_positive_number(userNumber):
        posOrNeg = "positive"
    else:
        posOrNeg = "negative"

    if is_fraction_in_number(userNumber):
        fract = "with fraction"
    else:
        fract = "without fraction"

    for i in range(len(userNumber)):
        if userNumber[i][:1] == "-":
            continue
        elif userNumber[i] != ".":
            digits += 1
        else:
            break

    if digits == 0:
        digits = 1

    res = {"number": userNumber,
           "digits": digits,
           "positive": posOrNeg,
           "fraction": fract}

    return res


def main():
    res = run()

    if res == -1:
        print("You entered not a number")
    elif isinstance(res, dict):
        print(f"User entered number: {res['number']}\n"
              f"It is:\n"
              f"{res['positive']}, {res['digits']}-digit {res['fraction']}")
    else:
        print("some error...")


if __name__ == "__main__":
    main()
