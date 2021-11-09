ukraine = ('kyiv', 'dnipro', 'lviv')
poland = ('warsaw','krakow', 'wroclaw')
france = ('paris', 'lion','marseille')
country_dict = {'UKRAINE':ukraine,'POLAND':poland, 'FRANCE':france}
while True:
    city = (input('enter the city\t\texit for close\n')).lower()
    if city == 'exit':
        break
    for key, values in country_dict.items():
        if city in values:
            print(key.capitalize())           