# Task 3
# Create a dictionary with the keys of which are the countries and the
# values of which are a list of the major cities of that country.
# When user enters the city, the program should display the country
# in which it is located.

countries = {"Ukraine": ["Kyiv", "Lviv", "Dnipro", "Rivne"],
             "USA": ["Washington", "LA", "NewYork", "Chicago"],
             "Croatia": ["Zagreb", "Dubrovnik", "Split", "Zadar"],
             "Italy": ["Roma", "Napoli", "Milano", "Venizia"],
             "Canada": ["Toronto", "Ottawa", "Montreal", "Quebec"],
             "England": ["London", "Liverpool", "Manchester", "Leeds"],
             }

userChoice = input("Enter the city: ")
for k, v in countries.items():
    for i in range(len(v)):
        if userChoice == v[i]:
            print("{} is in {}".format(userChoice, k))
            break
