# task_2
"""
кароч, тут трохи скопіювала і підредагувала під себе...
як всі :)))
але Українські міста воно не показує...
я не знаю...;)
"""
import requests


welcome = input("Welcome to the Python Weather Report Program: Press Enter to Continue")


def by_city():
    city = input('Please Enter Your City Name: ').title()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=3cfb3ef209130bbc71e87da6c0f41baf&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type Yes(1) or No(2): ')
    if question == '1':
        main()
    if question == '2':
        print("Thank you for using the program. Good Bye!")
        exit()
    else:
        print("well, that is not one of the options. Try again.")


def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))


def main():
    while True:
        answer = input("Want to know the weather? Please type yes(1) or no (2): ")
        if answer == "1":
            try:
                by_city()

            except Exception:
                print("hmm, You did not enter a valid name. Try again")
                by_city()
        if answer == "2":
            print("Thank you for using the program. Good Bye!")
            exit()
        else:
            print("well, that is not one of the options. Try again.")


main()
