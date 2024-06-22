import tkinter as tk
import requests
from datetime import datetime
from tkinter import *
from PIL import Image,ImageTk


def get_weather(root):
    city = textfield.get()
    apikey = "429992622d35f612d2d929e883655467"
    weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
    if requests.get(weather).json()['cod'] == "404":
        condensed_info="No city Found"
        condensed_data="No data Found"
    else:
        json_data = requests.get(weather).json()
        condition = json_data['weather'][0]['main']
        temp = json_data['main']['temp']
        feels_like = json_data['main']['feels_like']
        mintemp = json_data['main']['temp_min']
        maxtemp = json_data['main']['temp_max']
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = datetime.fromtimestamp(json_data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(json_data['sys']['sunset']).strftime('%H:%M')
        icon_id = json_data['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png" 

        image = Image.open(requests.get(icon_url,stream=True).raw)
        icon = ImageTk.PhotoImage(image)

        condensed_info = f"{condition}  {temp} °C\nFeel: {feels_like} °C"
        condensed_data = f"Min Temp: {mintemp}°C \tMaxTemp: {maxtemp}°C \tPressure: {pressure} hPa\nHumdity: {humidity}% \tWind: {wind}m/s \tSunrise: {sunrise} \tSunset: {sunset}"

        label_icon.config(image=icon)
        label_icon.image=icon
    label_info.config(text=condensed_info,bg = "#5a9bd8")
    label_desc.config(text=condensed_data,bg = "#5a9bd8")



root = tk.Tk()
root.geometry("900x400")
root.title("Uzair's Weather App")
root.configure(bg="#6cb2eb")
root.resizable(False,False)

#searchbox
textfield = tk.Entry(root,width=20,bg="#edf2f7",fg="#2b3649",font= ("Helvetica",20,"bold"),highlightthickness=2, highlightbackground="#cccccc", highlightcolor="lightblue")
textfield.pack(pady=20) #vertical padding of 20
textfield.focus() #to make the user directly enter city name w/out moving cursor
textfield.bind('<Return>',get_weather)
"""
Binding the <Return> event (which corresponds to pressing the Enter key) to a text field will allow you to trigger the get_weather function whenever the Enter key is pressed while the text field is focused
"""

label_info= tk.Label(root,bg="#6cb2eb",justify="center",font= ("Helevetica",20,"bold"),fg="#2b3649",width=53,height=3)
label_info.pack()


label_icon=tk.Label(root,bg="#6cb2eb",justify="center")
label_icon.pack()


label_desc=tk.Label(root,bg="#6cb2eb",justify="center",font = ("Helvetica",15),fg="#2b3649",width=90,height=20)
label_desc.pack()


root.mainloop() 
""" 
The mainloop function is used to start the Tk event loop. This event loop listens for events, such as button clicks or keyboard input, and handles them appropriately. Essentially, it keeps the application running, waiting for user interactions.

Waits for events such as key presses, mouse clicks, and other user interactions.
Dispatches events to the appropriate widget event handlers.
Updates the GUI based on these events.
Keeps the application running until you close the main window or call a method to exit the loop.

"""