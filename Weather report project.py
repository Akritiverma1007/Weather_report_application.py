from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

## Initialize the main window

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)



# Function to get weather details

def getWeather():
    try:
        city = textfield.get()           # Get city name from the input field

        geolocator = Nominatim(user_agent="unique_user_agent")
        location = geolocator.geocode(city)          # Get geographical coordinates for the city
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)        # Get timezone for the city
        print(result)

        # Get the current local time

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text = current_time)
        name.config(text = "CURRENT WEATHER")


        # WEATHER

        # Fetch weather data from OpenWeatherMap API

        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=94aaae693007ffe302a9be0f36d115bf"
        json_data = requests.get(api).json()

        # Extract relevant weather data

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)     # Convert temperature from Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update UI elements with weather data

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")



#Search box


Search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg='#404040', border=0, fg='white')
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor='hand2', bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#logo

logo_image = PhotoImage(file='Copy of logo.png')
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box

frame_image = PhotoImage(file="Copy of box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time display

name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helventica", 20))
clock.place(x=30, y=130)



# label for weather parameter

label1 = Label(root,text="WIND", font=("Helvetica", 15,'bold'),fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(root,text="HUMIDITY", font=("Helvetica", 15,'bold'),fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)

label3 = Label(root,text="DESCRIPTION", font=("Helvetica", 15,'bold'),fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)

label4 = Label(root,text="PRESSURE", font=("Helvetica", 15,'bold'),fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

# Display elements for weather data

t = Label(font=('arial', 70, 'bold'), fg='#ee666d')
t.place(x=400,y=150)

c = Label(font=('arial', 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=('arial', 20, 'bold'),bg='#1ab5ef')
w.place(x=120, y=430)

h = Label(text="...", font=('arial', 20, 'bold'),bg='#1ab5ef')
h.place(x=280, y=430)

d = Label(text="...", font=('arial', 20, 'bold'),bg='#1ab5ef')
d.place(x=450, y=430)

p = Label(text="...", font=('arial', 20, 'bold'),bg='#1ab5ef')
p.place(x=670, y=430)

# Start the main loop

root.mainloop()