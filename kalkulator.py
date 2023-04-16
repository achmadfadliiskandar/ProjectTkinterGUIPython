from tkinter import *
root = Tk()
root.title("SIMPLE KALKULATOR")

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def TombolKlik(angka):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(angka))

def TombolClear():
    e.delete(0,END)

def TombolTambah():
    nomorpertama = e.get()
    global nprtma
    global math
    math = "pertambahan"
    nprtma = int(nomorpertama)
    e.delete(0,END)

def TombolJumlah():
    nomorkedua = e.get()
    e.delete(0,END)
    if math == "pertambahan":
        e.insert(0,nprtma + int(nomorkedua))
    if math == "pengurangan":
        e.insert(0,nprtma - int(nomorkedua))
    if math == "perkalian":
        e.insert(0,nprtma * int(nomorkedua))
    if math == "pembagian":
        e.insert(0,nprtma / int(nomorkedua))

def TombolKurang():
    nomorpertama = e.get()
    global nprtma
    global math
    math = "pengurangan"
    nprtma = int(nomorpertama)
    e.delete(0,END)

def TombolKali():
    nomorpertama = e.get()
    global nprtma
    global math
    math = "perkalian"
    nprtma = int(nomorpertama)
    e.delete(0,END)

def TombolBagi():
    nomorpertama = e.get()
    global nprtma
    global math
    math = "pembagian"
    nprtma = int(nomorpertama)
    e.delete(0,END)


tombol1 = Button(root,text="1",padx=40,pady=20,command=lambda: TombolKlik(1))
tombol2 = Button(root,text="2",padx=40,pady=20,command=lambda: TombolKlik(2))
tombol3 = Button(root,text="3",padx=40,pady=20,command=lambda: TombolKlik(3))
tombol4 = Button(root,text="4",padx=40,pady=20,command=lambda: TombolKlik(4))
tombol5 = Button(root,text="5",padx=40,pady=20,command=lambda: TombolKlik(5))
tombol6 = Button(root,text="6",padx=40,pady=20,command=lambda: TombolKlik(6))
tombol7 = Button(root,text="7",padx=40,pady=20,command=lambda: TombolKlik(7))
tombol8 = Button(root,text="8",padx=40,pady=20,command=lambda: TombolKlik(8))
tombol9 = Button(root,text="9",padx=40,pady=20,command=lambda: TombolKlik(9))
tombol0 = Button(root,text="0",padx=40,pady=20,command=lambda: TombolKlik(0))
tomboltambah = Button(root,text="+",padx=39,pady=20,command=TombolTambah)
tombolsamadengan = Button(root,text="=",padx=91,pady=20,command=TombolJumlah)
tombolclear = Button(root,text="Clear",padx=79,pady=20,command=TombolClear)
tombolkurang = Button(root,text="-",padx=41,pady=20,command=TombolKurang)
tombolkali = Button(root,text="*",padx=40,pady=20,command=TombolKali)
tombolbagi = Button(root,text="/",padx=40,pady=20,command=TombolBagi)


# tampilkan baris grid dan tampilkan dilayar
tombol1.grid(row=3,column=0)
tombol2.grid(row=3,column=1)
tombol3.grid(row=3,column=2)

tombol4.grid(row=2,column=0)
tombol5.grid(row=2,column=1)
tombol6.grid(row=2,column=2)

tombol7.grid(row=1,column=0)
tombol8.grid(row=1,column=1)
tombol9.grid(row=1,column=2)

tombol0.grid(row=4,column=0)
tombolclear.grid(row=4,column=1,columnspan=2)
tomboltambah.grid(row=5,column=0)
tombolsamadengan.grid(row=5,column=1,columnspan=2)  
tombolkurang.grid(row=6,column=0)
tombolkali.grid(row=6,column=1)
tombolbagi.grid(row=6,column=2)
root.mainloop()