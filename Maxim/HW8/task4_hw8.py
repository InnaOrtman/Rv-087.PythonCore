# Task 4
# Create the function is_prime, which takes 1 argument - a number from
# 0 to 1000, and returns True if it is simple, and False - otherwise.

from mynum import is_positive_integer


def isPrime(number: int) -> bool:
    if number > 1:
        for i in range(2, number-1):
            if number % i == 0:
                return False
            return True
    return False


while True:
    num = input("Enter the number: ")
    if not is_positive_integer(num):
        print("You entered incorrect value")
        continue
    break

print(isPrime(int(num)))
