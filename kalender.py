from tkinter import *
import calendar

# config kalender
def fungsi():
    if __name__ == "__main__":
        root = Tk()
        variabel = dapatdata.get()
        teks = calendar.calendar(getint(variabel))
        # konfigurasi tampilan
        root.geometry("1280x800")
        root.title('Kalendar Fadli')
        label1 = Label(root,text="KALENDER",bg='dark gray',font=('times',28,'bold'))
        label1.grid(row=1,column=1)
        root.config(background='white')
        l1 = Label(root,text=teks,font="consolas 10 bold")
        l1.grid(row=2,column=1,padx=20)
        root.mainloop()
# end konfig kalender

# khusus inputanya
roots = Tk()
judulatas = roots.title("Kalender Fadli")
judul = Label(roots,text="masukan kalender yang ingin anda cari : ")
dapatdata = Entry(roots,bg='black',fg='white')
tombol = Button(roots,text='Cari\Search',bg='gold',fg='black',command=fungsi)
# tombolkeluar = Button(roots,text='Keluar\Exit',bg='red',fg='white',command=roots.destroy)
tombolkeluar = Button(roots,text='Keluar\Exit',bg='red',fg='white',command=exit)
judul.pack()
dapatdata.pack()
tombol.pack()
tombolkeluar.pack()
# end khusus inputanya
mainloop()