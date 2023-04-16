import tkinter as tkin
import datetime

root = tkin.Tk()
root.title("Jam Digital AF1")

def TangkapWaktu():
    waktusekarang = datetime.datetime.now()
    dekwaktu = waktusekarang.strftime("%H:%M:%S %p")
    tulisanjam.config(text=dekwaktu)
    tulisanjam.after(200,TangkapWaktu)

tulisanjam = tkin.Label(root,font=("Calibri",90),bg="black",fg='green')
tulisanjam.pack()

TangkapWaktu()

root.mainloop()