#Simple way to check things, more unneeded operations possible.

money_amount = int(input("Please enter the amount of money as real number.\n"))

money_amount_temp = money_amount

notes_200 = money_amount_temp // 200
money_amount_temp %= 200
print(money_amount_temp)

notes_100 = money_amount_temp // 100
money_amount_temp %= 100
print(money_amount_temp)

notes_10 = money_amount_temp // 10
money_amount_temp %= 10
print(money_amount_temp)


print(f"Exchange from {money_amount} UAH:\n{int(notes_200)} 200UAH notes\n{int(notes_100)} 100UAH notes\n{int(notes_10)} 10UAH notes\n{money_amount_temp} 1UAH coins")