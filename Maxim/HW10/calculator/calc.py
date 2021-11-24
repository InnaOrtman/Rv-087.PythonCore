from mynum import if_int_to_int


def mySum(*numArgs):
    if len(numArgs) > 1:
        return if_int_to_int(sum(numArgs))
    return "Not enough arguments to sum"


def myDiff(*numArgs):
    lenNumArgs = len(numArgs)
    res = float
    if len(numArgs) > 1:
        for i in range(lenNumArgs):
            if i == 0:
                res = numArgs[0]
                continue
            res -= numArgs[i]
        return if_int_to_int(res)
    return "Not enough arguments to sum"


def myProd(*numArgs):
    if len(numArgs) > 1:
        res = 1
        for i in range(len(numArgs)):
            res *= numArgs[i]
        return if_int_to_int(res)
    return "Not enough arguments to product"


def myFraction(*numArgs):
    lenNumArgs = len(numArgs)
    res = float
    if lenNumArgs > 1:
        for i in range(lenNumArgs):
            if i == 0:
                res = numArgs[0]
                continue
            if numArgs[i] == 0:
                return "You can't devide on 0"
            res /= numArgs[i]
        return if_int_to_int(res)
    return "Not enough arguments to product"
