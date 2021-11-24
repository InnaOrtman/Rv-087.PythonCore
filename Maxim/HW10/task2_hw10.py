import rsa
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps


privkey = rsa.PrivateKey(9977144127109373496924818538232893438461065171336219244913776687448055681355829843789031461225328264601368353770733975344261816197279617687661585697985949, 65537, 9048195083613006603746381278054717510946998008123169977592052083837758655427992479560593492511713487398341822966359165065680493000389162983030723317024373, 7076628309057671289612499699368506089977691296868274259546081333342641371573480711, 1409872568033453334752082789548131757286292890717548001272438662613984059)
enctex = b'~\x7f\xf47\x05\xe1\xb0\xb0Q\xae\x84\x91\x16\x19\xf8\n\x1ffE\xbc\xcf! +\x95a\x87\xd2\x1a\xca\xb9:>n\xb0f\x8a\xae\x9c\x9d\xdaB\xddI\xea\x89\xf8\xf1\x82C\x02\x97\xe0\xef\x10\x99,\xda\x9f\x92\x82\t)f'
dectex = rsa.decrypt(enctex, privkey).decode()
config_dict = get_default_config()
config_dict['language'] = 'ua'
city = input("Enter city name: ")

owm = OWM(dectex)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
weather = observation.weather
wind_dict_in_meters_per_sec = weather.wind()

# today
temperature = weather.temperature('celsius')['temp']
print(f"In {city} today:\ntemperature: {str(temperature)} Celsius\n"
      f"{weather.detailed_status}\n"
      f"wind speed: {wind_dict_in_meters_per_sec['speed']}\n"
      f"visibility distance: {weather.visibility_distance}\n"
      f"pressure: {weather.pressure['press']}\n")

# tomorow
tomorrow = timestamps.tomorrow()
daily_forecaster = mgr.forecast_at_place(city, '3h')
weather = daily_forecaster.get_weather_at(tomorrow)
print(f"Tomorow will be:\n"
      f"temperature: {weather.temperature('celsius')['temp']} Celsius\n"
      f"{weather.detailed_status}\n"
      f"wind speed: {wind_dict_in_meters_per_sec['speed']}\n"
      f"visibility distance: {weather.visibility_distance}\n"
      f"pressure: {weather.pressure['press']}\n")
