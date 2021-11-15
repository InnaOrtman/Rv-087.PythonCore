countries = dict()

countries['Ukraine'] = ['Lviv', 'Kyiv', 'Kharkiv']
countries['Deutschland'] = ['Berlin', 'München', 'Hamburg']
countries['Netherlands'] = ['Amsterdam', 'Rotterdam' 'The Hague']
countries['Austria'] = ['Vienna', 'Graz', 'Linz']
countries['Italy'] = ['Rome', 'Milan', 'Naples']


city = str(input('Enter the city: '))

for i in countries.keys():
    if city in countries[i]:
        print('It is ', i)
        break
else:
    print('Enter other city')