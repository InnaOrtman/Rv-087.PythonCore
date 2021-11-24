# Task 1
# Create a function calculator(arg) that takes 1 argument: 1, 2, 3, 4.
# This function should return function sum(a,b) if arg = 1, dif(a,b)
# if arg = 2, product(a,b) if arg = 3 and fraction(a,b) if arg=4.

from mynum import if_int_to_int


def calculator(numFunction: int, numArgs: tuple) -> [int, tuple]:
    """To calculate sum first argument must be 1, to diff - 2, to
    product - 3 and to fraction - 4. Second argument must be a
    tuple of numbers which you want to calculate"""

    notEnArgs = "Not enough arguments to sum"

    def mySum(args: tuple) -> [int, tuple, str]:
        if len(args) > 1:
            return if_int_to_int(sum(args))
        return notEnArgs

    def myDiff(args: tuple) -> [int, tuple, str]:
        lenNumArgs = len(args)
        res = float
        if len(args) > 1:
            for i in range(lenNumArgs):
                if i == 0:
                    res = args[0]
                    continue
                res -= args[i]
            return if_int_to_int(res)
        return notEnArgs

    def myProd(args: tuple) -> [int, tuple, str]:
        if len(args) > 1:
            res = 1
            for i in range(len(args)):
                res *= args[i]
            return if_int_to_int(res)
        return notEnArgs

    def myFraction(args: tuple) -> [int, tuple, str]:
        lenNumArgs = len(args)
        res = float
        if lenNumArgs > 1:
            for i in range(lenNumArgs):
                if i == 0:
                    res = args[0]
                    continue
                if args[i] == 0:
                    return "You can't devide on 0"
                res /= args[i]
            return if_int_to_int(res)
        return notEnArgs

    if numFunction == 1:
        return mySum(numArgs)
    if numFunction == 2:
        return myDiff(numArgs)
    if numFunction == 3:
        return myProd(numArgs)
    if numFunction == 4:
        return myFraction(numArgs)


def genToHundred():
    for i in range(100):
        yield str(i) + " ->"


num = genToHundred()

print(num.__next__(), calculator(1, (10, 1)))
print(num.__next__(), calculator(2, (10, 1)))
print(num.__next__(), calculator(3, (10, 1)))
print(num.__next__(), calculator(4, (10, 1)))
print(num.__next__(), calculator(1, (10, 1, 3.2)))
print(num.__next__(), calculator(2, (10, 1, 3.2)))
print(num.__next__(), calculator(3, (10, 1, 3.2)))
print(num.__next__(), calculator(4, (10,)))
print(num.__next__(), calculator(4, (0, 1)))
print(num.__next__(), calculator(4, (1, 0)))
