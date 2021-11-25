import tkinter as tk
from pyowm import OWM


root = tk.Tk()


def getWeather():
    """ Get weather details from OPW using PyOPW for entered locality """
    owm = OWM('cc7ee943e8c6c3a36724c9d48c490c2b')
    city = cityField.get()
    mgr = owm.weather_manager()
    # If locality exist, weather details will be added to according label
    # If not exist, wrong entry message
    try:
        weather = mgr.weather_at_place(city).weather
        resultLabel['text'] = 'Weather status: {}'.format(weather.detailed_status)
        resultLabel2['text'] = 'Temperature: {}C'.format(weather.temperature(unit="celsius")['temp'])
        resultLabel3['text'] = 'Wind speed: {} m/sec'.format(weather.wind()['speed'])
        resultLabel4['text'] = 'Humidity: {}%'.format(weather.humidity)
    except:
        resultLabel['text'] = ''
        resultLabel2['text'] = 'Nothing found, '
        resultLabel3['text'] = 'check your entry.'
        resultLabel4['text'] = ''

# Configuring application window
root['bg'] = '#344A5F'
root.title("What's the weather in...")
root.geometry('350x300')
root.resizable(width=False, height=False)


# Adding GUI elements to application window
frameTop = tk.Frame(root, bg='#2a94d6')
frameTop.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.4)
label1 = tk.Label(frameTop, text='Enter your city:', bg='#2a94d6')
label1.pack()
cityField = tk.Entry(frameTop, bd=3, font=20)
cityField.pack()
button1 = tk.Button(frameTop, text='Check the weather', command=getWeather)
button1.pack(side='bottom', pady=20)

labelframe_widget = tk.LabelFrame(root, text="Weather result", bg='#2a94d6')
labelframe_widget.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.4)

resultLabel = tk.Label(labelframe_widget, text="",
                       bg='#2a94d6', font=('Times new Roman', 10))
resultLabel.pack()
resultLabel2 = tk.Label(labelframe_widget, text="",
                        bg='#2a94d6', font=('Times new Roman', 10))
resultLabel2.pack()
resultLabel3 = tk.Label(labelframe_widget, text="",
                        bg='#2a94d6', font=('Times new Roman', 10))
resultLabel3.pack()
resultLabel4 = tk.Label(labelframe_widget, text="",
                        bg='#2a94d6', font=('Times new Roman', 10))
resultLabel4.pack()

root.mainloop()
