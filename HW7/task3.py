country_dict = {"USA": ("New York", "Washington", "Los Angeles"), "England":\
("London, Briton, Bath"), "Ukraine": ("Kyiv, Kharkiv, Dnipro")}

print(country_dict.values())
user_input = input("Please enter a city from cities in our base.\n")

for i in country_dict.keys():
    if user_input in country_dict[i]:
        print(f"This city is in {i}.")
        break
else:
    print("We don't have this city in our base.")
