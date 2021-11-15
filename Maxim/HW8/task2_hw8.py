# Task 2
# The user makes a deposit of n dollars for year at 10% per annum (each
# year the amount of his deposit increases by 10%. This money is added
# to the deposit amount, and next year there will also be interest on it).
# Create a bank function that takes the arguments n and years and
# returns the amount that will be in the user's account.

from mynum import if_int_to_int
from mynum import is_positive_integer
from mynum import is_positive_number
# from mynum import is_number


def deposit(money: str,
            years: str,
            percent: float = 10) -> [int, float]:
    if not is_positive_number(str(money)) \
            or not is_positive_integer(str(years)):
        return "You entered incorrect data"

    def calc(money_=float(money), years_=int(years), percent_=percent):
        money_ = money_ / 100 * percent_ + money_
        years_ -= 1
        if years_ == 0:
            return money_
        else:
            return calc(money_=money_, years_=years_, percent_=percent)

    return if_int_to_int(calc())


# print(deposit(100, 1, 10))
print(deposit(input("Enter a value of your deposit: "),
              input("Enter number of years: "),
              15.7))
