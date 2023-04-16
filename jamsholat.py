import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

root = tk.Tk()
root.title("JAM SHOLAT GUI TKINTER")
root.configure(bg="#d6e4f0")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# logo aplikasi ini
icon_image = Image.open("jammasjid.jpeg")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)


# Fetch the list of cities from the API URL
url = "https://api.banghasan.com/sholat/format/json/kota"
response = requests.get(url)
data = response.json()

# Get the list of cities from the data
cities = data["kota"]

# Create a list of city names and IDs
city_names = []
city_ids = []
for city in cities:
    city_names.append(city["nama"])
    city_ids.append(city["id"])

# Create a ComboBox to display the city names
city_var = tk.StringVar()
city_combobox = tk.ttk.Combobox(root, textvariable=city_var, values=city_names)
city_combobox.current(0)
city_combobox.grid(row=0, column=0, padx=10, pady=10)

# Create a function to fetch and display the prayer times for the selected city
def get_prayer_times():
    # Get the ID of the selected city
    selected_city_name = city_var.get()
    selected_city_index = city_names.index(selected_city_name)
    selected_city_id = city_ids[selected_city_index]

    # Fetch the prayer times for the selected city
    x = datetime.datetime.now()
    date = x.strftime("%Y-%m-%d")  # You can modify this to use a different date
    url = "https://api.banghasan.com/sholat/format/json/jadwal/kota/{}/tanggal/{}".format(selected_city_id, date)
    response = requests.get(url)
    data = response.json()

    # Get the prayer times from the data
    prayer_times = data["jadwal"]["data"]

    # Display the prayer times in Labels
    fajr_label.config(text="Subuh: {}".format(prayer_times["subuh"]))
    dhuhr_label.config(text="Dzuhur: {}".format(prayer_times["dzuhur"]))
    asr_label.config(text="Ashar: {}".format(prayer_times["ashar"]))
    maghrib.config(text="Magrib: {}".format(prayer_times["maghrib"]))
    isya.config(text="Isya: {}".format(prayer_times["isya"]))
    imsak.config(text="Imsak: {}".format(prayer_times["imsak"]))
    subuh.config(text="Subuh: {}".format(prayer_times["subuh"]))
    terbit.config(text="Terbit: {}".format(prayer_times["terbit"]))
    dhuha.config(text="Dhuha: {}".format(prayer_times["dhuha"]))
    tanggal.config(text="Tanggal: {}".format(prayer_times["tanggal"]))

# Create Buttons to fetch and display the prayer times
get_times_button = tk.Button(root, text="Tampilkan Waktu Sholat", command=get_prayer_times)
get_times_button.grid(row=10, column=0, padx=10, pady=10)

# Create Labels to display the prayer times
fajr_label = tk.Label(root, text="Subuh: ",font=('Helvetica bold',26),height=3,width=25)
fajr_label.grid(row=0, column=1, padx=10, pady=10)

dhuhr_label = tk.Label(root, text="Dzuhur: ",font=('Helvetica bold', 26),height=3,width=15)
dhuhr_label.grid(row=0, column=2, padx=10, pady=10)

asr_label = tk.Label(root, text="Ashar: ",font=('Helvetica bold', 26),height=3,width=12)
asr_label.grid(row=1, column=0, padx=10, pady=10)

maghrib = tk.Label(root, text="Magrib: ",font=('Helvetica bold', 26),height=3,width=25)
maghrib.grid(row=1, column=1, padx=10, pady=10)

imsak = tk.Label(root, text="Imsak: ",font=('Helvetica bold', 26),height=3,width=15)
imsak.grid(row=1, column=2, padx=10, pady=10)

isya = tk.Label(root, text="Isya: ",font=('Helvetica bold', 26),height=3,width=12)
isya.grid(row=2, column=0, padx=10, pady=10)

subuh = tk.Label(root, text="Subuh: ",font=('Helvetica bold', 26),height=3,width=25)
subuh.grid(row=2, column=1, padx=10, pady=10)

terbit = tk.Label(root, text="Terbit: ",font=('Helvetica bold', 26),height=3,width=15)
terbit.grid(row=2, column=2, padx=10, pady=10)

dhuha = tk.Label(root, text="Dhuha: ",font=('Helvetica bold', 26),height=3,width=12)
dhuha.grid(row=3, column=0, padx=10, pady=10)

tanggal = tk.Label(root, text="Tanggal: ",font=('Helvetica bold', 26),height=3,width=25)
tanggal.grid(row=3, column=1, padx=10, pady=10)

def TangkapWaktu():
    waktusekarang = datetime.datetime.now()
    dekwaktu = waktusekarang.strftime("%H:%M:%S %p")
    tulisanjam.config(text=dekwaktu)
    tulisanjam.after(200,TangkapWaktu)

tulisanjam = tk.Label(root,font=("Helvetica bold",26),height=3,width=15)
tulisanjam.grid(row=3, column=2, padx=10, pady=10)

TangkapWaktu()

root.mainloop()