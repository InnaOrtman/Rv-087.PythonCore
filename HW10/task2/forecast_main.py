from pyowm.owm import OWM
owm = OWM('<token>')
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=50.4501, lon=30.5234)

kyiv = one_call.forecast_daily[0].temperature('celsius')

print("Kyiv weather forecast for today:")
for keys, values in kyiv.items():
    print(keys, values)