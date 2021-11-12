def bankFunction(deposit, years):
    youWillGet = 0
    for i in range(years):
        percents = deposit/100*10
        deposit = deposit + percents
        youWillGet += deposit

print(bankFunction(1000,4))