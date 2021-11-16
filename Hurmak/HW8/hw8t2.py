def countDepo(amount, years):
    if years == 0:
        return amount
    return countdepo(amount, years-1)*1.10


print(countdepo(100, 1))
