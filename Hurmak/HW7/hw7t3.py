countries = {'Ukraine': ['Kyiv', 'Lviv', 'Rivne'], 'Gabon': ['Libreville', 'Makokou']}
found = False
while True:
    city = input("Enter a city: ")
    for i in countries.keys():
        if city in countries[i]:
            found = i
    if found:
        print(f'{city} found in {found}')
        break
    else:
        print('Nothing found, try again')
