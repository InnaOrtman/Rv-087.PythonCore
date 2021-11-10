def simpleCheck(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


print(simpleCheck(13))
