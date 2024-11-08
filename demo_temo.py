from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    api_key = "f212bc312404d83015ecdc7e54bba3be"  # Consider hiding or using an environment variable for security.
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}").json()
        if data.get("cod") != 200:
            raise ValueError("City not found or API error.")
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15))) # Corrected this line
        per_label1.config(text=(data["main"]["pressure"]))
    except Exception as e:
        print(f"Error: {e}")
        return


win = Tk()
win.title("ROJA SHRESTHA")
win.config(bg="blue")
win.geometry("500x570")  # Corrected this line

name_label = Label(win, text="ROJA Weather APP", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = [
    "Kathmandu", "Pokhara", "Lumbini", "Chitwan", "Bhaktapur", "Patan", "Nagarkot", "Dhulikhel",
    "Sagarmatha National Park", "Bandipur", "Rara Lake", "Mustang", "Manang", "Janakpur", "Palpa",
    "Gosaikunda", "Langtang National Park", "Ilam", "Biratnagar", "Birgunj", "Hetauda", "Namche Bazaar",
    "Sauraha", "Tansen", "Gorkha", "Kakani", "Khaptad National Park", "Jomsom", "Annapurna Base Camp",
    "Dharan", "Phaplu", "Simikot", "Darchula", "Makalu Barun National Park", "Pashupatinath Temple",
    "Swayambhunath (Monkey Temple)", "Bouddhanath Stupa", "Koshi Tappu Wildlife Reserve", "Bardiya National Park",
    "Shuklaphanta National Park", "Rupandehi", "Butwal", "Tengboche Monastery", "Pimbahal",
]

com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Time New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Time New Roman", 17))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Time New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Time New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Time New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="DONE", font=("Time New Roman", 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
