import tkinter as tkin
from tkinter import ttk
first = tkin.Tk()
# untuk mencetak label
a = tkin.Label(first,text="Assalamualaikum wr wb")
# untuk mencetak button
# saya pakai fungsi supaya dapat inputan dari user ketika tombol diklik
def kunci():
    getbtn = tkin.Label(first,text=c.get())
    getbtn.pack()
    getcombo = tkin.Label(first,text=d.get())
    getcombo.pack()
    dapatmenuradio = var.get()
    if dapatmenuradio == 0:
        tampilan = "HTML"
    elif dapatmenuradio == 1:
        tampilan = "CSS"
    elif dapatmenuradio == 2:
        tampilan = "JAVASCRIPT"
    gete = tkin.Label(first,text=tampilan)
    gete.pack()

b = tkin.Button(first,text="Klik aku dong",command=kunci)
# untuk membuat form input
c = tkin.Entry(first,bg="black",fg="white")
# untuk membuat form select/combobox
data = ['php','javascript','python','java']
d = ttk.Combobox(first,values=data)
def search(event):
    value = event.widget.get()
    if value == '':
        d['value'] = data
    else:
        kumpulandata = []

        for item in data:
            if value.lower() in item.lower():
                kumpulandata.append(item)
        d['value'] = kumpulandata
# untuk membuat fungsi search tapi tidak masuk ke dalam button 
d.set('Search')
# # untukk membuat radio button
var = tkin.IntVar()
# radio 1 yang bernilai0 sd 2
e = ttk.Radiobutton(first,text='html',variable=var,value=0)
e1 = ttk.Radiobutton(first,text='css',variable=var,value=1)
e2 = ttk.Radiobutton(first,text='javascript',variable=var,value=2)
a.pack()
c.pack()
d.pack()
d.bind('<KeyRelease>',search)
e.pack()
e1.pack()
e2.pack()
b.pack()
first.mainloop()