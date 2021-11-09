# task_3
"""
словник зробила мінімальний
для швидкої звірки даних
"""
Capitals = dict()

Capitals['France'] = ['Paris', 'Marcel']
Capitals['Ukraine'] = ['Kyiv', "Lviv"]
Capitals['USA'] = ['Washington', 'New York']

x = input("Enter the city name:\n").title()

for key, value in Capitals.items():
    if x in value:
        print(f"You are in {key} now")



