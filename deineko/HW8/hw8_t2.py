def bankFunction(deposit, years):
    youWillGet = deposit * (1 + 10/100)**years
    return youWillGet

print(bankFunction(1000,4))