# Importing necessary modules
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from plyer import notification
import requests
import time

# Function to get a notification of the weather report
def getNotification():
    cityName = place.get()  # Getting input of the name of the place from the user
    apiKey = 'fa504bd297d010e25c52f7b918033e2f'  # Replace with your OpenWeatherMap API key
    baseUrl = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"

    try:
        response = requests.get(baseUrl)  # Requesting for the content of the URL
        data = response.json()  # Converting it into JSON

        # Getting the required information from the JSON response
        temp = data["main"]["temp"] - 273.15  # Converting temperature from Kelvin to Celsius
        pres = data["main"]["pressure"]
        hum = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        # Combining the information as a string
        info = f"Here is the weather description of {cityName}:\nTemperature = {temp:.2f}°C\nAtmospheric pressure = {pres}hPa\nHumidity = {hum}%\nDescription of the weather= {weather_desc}"

        # Showing the notification
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=2
        )

        # Waiting time
        time.sleep(7)

    except Exception as e:
        messagebox.showerror('spell the correct word', e)  # Show a pop-up message if any error occurred

# Creating the window
wn = Tk()
wn.title("Python Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="Python Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Getting the city name
Label(wn, text='Enter the Location:', font=("Courier", 10), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get a notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification)
btn.place(relx=0.4, rely=0.75)

# Run the window until closed by the user
wn.mainloop()
