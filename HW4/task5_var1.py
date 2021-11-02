#More complex, but less checks.

money_amount = int(input("Please enter the amount of money as real number.\n"))
money_amount_temp = money_amount
notes_200 = 0
notes_100 = 0
notes_10 = 0
coins_1 = 0

if money_amount_temp % 200 == 0:
    notes_200 = money_amount_temp // 200
else:
    notes_200 = money_amount_temp // 200
    money_amount_temp %= 200
    if money_amount_temp % 100 == 0:
        notes_100 = money_amount_temp // 100
    else:
        notes_100 = money_amount_temp // 100
        money_amount_temp %= 100
        if money_amount_temp % 10 == 0:
            notes_10 = money_amount_temp // 10
        else:
            notes_10 = money_amount_temp // 10
            money_amount_temp %= 10
            
print(f"Exchange from {money_amount} UAH:\n{int(notes_200)} 200UAH notes\n{int(notes_100)} 100UAH notes\n{int(notes_10)} 10UAH notes\n{money_amount_temp} 1UAH coins")