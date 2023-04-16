import tkinter as tkin
from urllib import request
import json

root = tkin.Tk()
root.title("IP TRACKER")
root.geometry("1000x1000")

# JUDUL 
judul = tkin.Label(root,text='IP TRACKER',font=("Helvetica",35))
judul.pack()

url = "https://ipapi.co/"
request = request.urlopen(url + "/json")
data_json = json.loads(request.read())

for data in data_json:
    info = str(data_json[data])
    cetakontent = tkin.Label(root,text=str.upper(data + " : " + info))
    cetakontent.pack()

root.mainloop()