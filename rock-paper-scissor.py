from tkinter import * 
from tkinter import ttk
import random
from PIL import Image,ImageTk


# untuk mengkonfigurasi halaman
root = Tk()
root.geometry("1000x1000")
root.title("GUNTING BATU KERTAS")

# logo aplikasi ini
icon_image = Image.open("gbk.png")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

# make score 
scoreplayer = 0
scorecomputer = 0

# selesai game (karena kasusnya masih dasar makanya
# kasih poin 5 menang singkatnya siapa yg lima duluan
# maka dia menang)
poinakhir = 5

# logika lawan / ai karena  ini (komputer)
# jenisnya ai weak jadi dia hanya mengetahui yang kita berikan
# BATU
# GUNTING
# KERTAS

#selain itu dia tidak akan mengetahuinya

# membuat judul
judul = Label(root,text=f"Road To {poinakhir} poin",font=("Verdana",32,"bold"))
judul.pack()

# keterangan
hasil = Label(root,text=f"Data Tidak ada",font=("Verdana",26,"bold"))
hasil.pack()

konfirmasi = Label(root,text=f"Data Tidak ada",font=("Verdana",26,"bold"))
konfirmasi.pack()

# fungsi restart
def Restart():
    global scorecomputer,scoreplayer
    scorecomputer = 0
    angkakomputer.config(text=scorecomputer)
    scoreplayer = 0
    angkaplayer.config(text=scoreplayer)
    tombol.config(state=NORMAL)



# fungsi setelah diklik
def Fungsi():
    global scoreplayer
    global scorecomputer
    # hasil pilihan pemain
    pilihanplayer = opsi_pilihan.get()
    # logika pilihan komputer
    pilihankomputer = random.choice(["BATU", "GUNTING", "KERTAS"])
    #PLAYER MEMILIH BATU
    if pilihanplayer == "BATU" and pilihankomputer == "GUNTING":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kamu Menang")
        scoreplayer += 1
        angkaplayer.config(text=scoreplayer)
    if pilihanplayer == "BATU" and pilihankomputer == "KERTAS":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kamu Kalah")
        scorecomputer += 1
        angkakomputer.config(text=scorecomputer)
    if pilihanplayer == "BATU" and pilihankomputer == "BATU":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kalian Seri")
        # pass
    
    #PLAYER MEMILIH KERTAS
    if pilihanplayer == "KERTAS" and pilihankomputer == "GUNTING":
        scorecomputer += 1
        angkakomputer.config(text=scorecomputer)
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kamu Kalah")
    if pilihanplayer == "KERTAS" and pilihankomputer == "BATU":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kamu Menang")
        scoreplayer += 1
        angkaplayer.config(text=scoreplayer)
    if pilihanplayer == "KERTAS" and pilihankomputer == "KERTAS":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kalian Seri")
        # pass

    #PLAYER MEMILIH GUNTING
    if pilihanplayer == "GUNTING" and pilihankomputer == "BATU":
        scorecomputer += 1
        angkakomputer.config(text=scorecomputer)
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kamu Kalah")
    if pilihanplayer == "GUNTING" and pilihankomputer == "KERTAS":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kamu Menang")
        scoreplayer += 1
        angkaplayer.config(text=scoreplayer)
    if pilihanplayer == "GUNTING" and pilihankomputer == "GUNTING":
        hasil.config(text=pilihanplayer +":"+ pilihankomputer)
        konfirmasi.config(text="Kalian Seri")
        # pass
    if scoreplayer == poinakhir or scorecomputer == poinakhir:
        tombol.config(state=DISABLED)
        tombolrestart.config(state=NORMAL)

# make grid 3x3
# for player
player = Label(root,text="PLAYER",font=("Verdana",26,"bold"))
angkaplayer = Label(root,text=scoreplayer,font=("Verdana",32,"bold"))
# player.grid(row=0,column=0)
player.place(relx=0.3,rely=0.5,anchor=CENTER)
angkaplayer.place(relx=0.3,rely=0.6,anchor=CENTER)

# print vs
versus = Label(root,text="VS",font=("Verdana",26,"bold"))
versus.place(relx=0.5,rely=0.5,anchor=CENTER)

# for comp
computer = Label(root,text="COMPUTER",font=("Verdana",26,"bold"))
angkakomputer = Label(root,text=scorecomputer,font=("Verdana",32,"bold"))
computer.place(relx=0.7,rely=0.5,anchor=CENTER)
angkakomputer.place(relx=0.7,rely=0.6,anchor=CENTER)
# computer.grid(row=0,column=2)
# player.place(relx=0.3,rely=0.7,anchor=CENTER)

# untuk pemilihan kategori / baris yang dipilih oleh
# player
opsi = ["GUNTING","BATU","KERTAS"]
opsi_pilihan = StringVar()
opsi_pilihan.set(opsi[0])
comboboks = ttk.Combobox(root,textvariable=opsi_pilihan,values=opsi)
comboboks.place(relx=0.5,rely=0.7,anchor=N)

# untuk submit pilihan dari opsi
tombol = Button(root,text='Submit',command=Fungsi)
tombol.place(relx=0.6,rely=0.7,anchor=N)
# tombol.pack() 

# tombol restart
tombolrestart = Button(root,text='Restart',command=Restart,state=DISABLED)
tombolrestart.place(relx=0.7,rely=0.7,anchor=N)

# tombol keluar exit
tombolkeluar = Button(root,text='Exit',command=exit)
tombolkeluar.place(relx=0.8,rely=0.7,anchor=N)

root.mainloop()