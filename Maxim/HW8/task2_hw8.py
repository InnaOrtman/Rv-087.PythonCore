# Task 2
# The user makes a deposit of n dollars for year at 10% per annum (each
# year the amount of his deposit increases by 10%. This money is added
# to the deposit amount, and next year there will also be interest on it).
# Create a bank function that takes the arguments n and years and
# returns the amount that will be in the user's account.

from mynum import if_int_to_int
from mynum import is_positive_natural
from mynum import is_positive_number


def deposit(money: float,
            years: [int],
            percent: int = 10) -> [int, float]:
    if not is_positive_number(str(money)) \
            or not is_positive_natural(str(years)) \
            or not is_positive_natural(str(percent)):
        return "You entered incorrect data"

    def calc(money_=money, years_=years, percent_=percent):
        allMoney = money_
        res = 0
        res += allMoney / 100 * percent_
        allMoney += res
        years_ -= 1
        if years_ == 0:
            return allMoney
        else:
            return calc(money_=allMoney, years_=years_, percent_=percent)

    return if_int_to_int(calc())


# print(deposit(100, 1, 10))
print(deposit(float(input("Enter a value of your deposit: ")),
              int(input("Enter number of years: ")),
              10))
