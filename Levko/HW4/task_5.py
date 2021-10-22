# task_5

money = int(input("Enter the amount of money (UAH): "))

if money % 200 == 0:
    print(f"You will have: {round(money/200)} 200/banknotes")
elif money < 200:
    print(f"You will have: 0 200/banknotes")
elif money % 200 != 1:
    print(f"You will have: {round(money/200)-1} 200/banknotes")

if money % 100 == 0:
    print(f"You will have: {round(money/100)} 100/banknotes")
elif money < 100:
    print(f"You will have: 0 100/banknotes")
elif money % 100 != 1:
    print(f"You will have: {round(money/100)-1} 100/banknotes")
elif money == money:
    print(f"You will have: {money}  1/banknotes")

if money % 10 == 0:
    print(f"You will have: {round(money/10)} 10/banknotes")
elif money < 10:
    print(f"You will have: 0 10/banknotes")
elif money % 10 != 1:
    print(f"You will have: {round(money/10)-1} 10/banknotes")

if money == money:
    print(f"You will have: {money}  1/banknotes")


