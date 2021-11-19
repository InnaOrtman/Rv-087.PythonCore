from pyowm.owm import OWM
owm = OWM('def83917c28a5e028dbc7d6b45bb3094')
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=50.4501, lon=30.5234)

kyiv = one_call.forecast_daily[0].temperature('celsius')

print("Kyiv weather forecast for today:")
for keys, values in kyiv.items():
    print(keys, values)