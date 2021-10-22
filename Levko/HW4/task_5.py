# task_5

money = int(input("Enter the amount of money (UAH): "))

if money < 200:
    print(f"You will have: 0 200/banknotes")
else:
    print(f"You will have: {int( money / 200)} 200/banknotes")

if money < 100:
    print(f"You will have: 0 100/banknotes")
else:
    print(f"You will have: {int( money / 100)} 100/banknotes")

if money < 10:
    print(f"You will have: 0 10/banknotes")
else:
    print(f"You will have: {int( money / 10)} 10/banknotes")

if money == money:
    print(f"You will have: {money}  1/banknotes")
