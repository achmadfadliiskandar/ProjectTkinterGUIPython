from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('TIC TAC TOE')

# konsep menang game 3X3
# 123,456,789 konsep datar samping 
# 147,258,369 konsep datar belakang
# 159,753,951 konsep datar miring samping kanan kiri

# fungsi untuk button JANGAN DIGANGGU
# konsep aja ini mah
def start_game():
    selected_value = combobox.get()
    if selected_value == "":
        messagebox.showerror("Tejadi Kesalahan", "Pilih angka 1-2 terlebih dahulu!")
    else:
        info_label.config(text="Keterangan: 1:Bulat 2:Silang")
        dd = int(selected_value)
        jumlahklik.set(dd)
        start_button.config(state=DISABLED)
        tombol1.config(state=NORMAL)
        tombol2.config(state=NORMAL)
        tombol3.config(state=NORMAL)
        tombol4.config(state=NORMAL)
        tombol5.config(state=NORMAL)
        tombol6.config(state=NORMAL)
        tombol7.config(state=NORMAL)
        tombol8.config(state=NORMAL)
        tombol9.config(state=NORMAL)

info_label = Label(root, text="Pilih Angka 1-2")
info_label.grid(row=0,column=0)

combobox = ttk.Combobox(root, values=[1, 2])
combobox.grid(row=0,column=1)

start_button = Button(root, text="Mulai", command=start_game)
start_button.grid(row=0,column=2)

jumlahklik =  IntVar()

# restart
def Restart():
    # pass
    tombol1.config(text="",state=DISABLED)
    tombol2.config(text="",state=DISABLED)
    tombol3.config(text="",state=DISABLED)
    tombol4.config(text="",state=DISABLED)
    tombol5.config(text="",state=DISABLED)
    tombol6.config(text="",state=DISABLED)
    tombol7.config(text="",state=DISABLED)
    tombol8.config(text="",state=DISABLED)
    tombol9.config(text="",state=DISABLED)
    start_button.config(state=NORMAL)

# menonaktifkan tombol stelah menang
def disabledall():
    tombol1.config(state=DISABLED)
    tombol2.config(state=DISABLED)
    tombol3.config(state=DISABLED)
    tombol4.config(state=DISABLED)
    tombol5.config(state=DISABLED)
    tombol6.config(state=DISABLED)
    tombol7.config(state=DISABLED)
    tombol8.config(state=DISABLED)
    tombol9.config(state=DISABLED)
    restart_button.config(state=NORMAL)

# check kondisi menang
def checkmenang():
    # KONDISI DATAR
    if tombol1['text'] == tombol2['text'] == tombol3['text']:
        return tombol1['text']
        # tombol1.config(bg='red')
        # tombol2.config(bg='red')
        # tombol3.config(bg='red')
    if tombol4['text'] == tombol5['text'] == tombol6['text']:
        return tombol4['text']
    if tombol7['text'] == tombol8['text'] == tombol9['text']:
        return tombol7['text']
    # KONDISI DATAR

    # KONDISI BAWAH ATAS
    if tombol1['text'] == tombol4['text'] == tombol7['text']:
        return tombol1['text']
    if tombol2['text'] == tombol5['text'] == tombol8['text']:
        return tombol2['text']
    if tombol3['text'] == tombol6['text'] == tombol9['text']:
        return tombol3['text']
    # KONDISI BAWAH ATAS

    # KONDISI MIRING KIRI
    if tombol1['text'] == tombol5['text'] == tombol9['text']:
        return tombol1['text']
    # KONDISI MIRING KANAN
    if tombol3['text'] == tombol5['text'] == tombol7['text']:
        return tombol3['text']
    return None

def Buttonn1():
    global jumlahklik
    # global pemenang
    jumlahklik.set(jumlahklik.get() + 1)
    # print(jumlahklik)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol1['state'] = DISABLED
        tombol1.config(text="X",font=20)
        print(tombol1['text'])
    else:
        tombol1['state'] = DISABLED
        tombol1.config(text="O",font=20)
        print(tombol1['text'])
    pemenang = checkmenang()
    if pemenang:
        # print("pemenangnya adalah : " + pemenang)
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn2():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol2['state'] = DISABLED
        tombol2.config(text="X",font=20)
    else:
        tombol2['state'] = DISABLED
        tombol2.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn3():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol3['state'] = DISABLED
        tombol3.config(text="X",font=20)
    else:
        tombol3['state'] = DISABLED
        tombol3.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn4():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol4['state'] = DISABLED
        tombol4.config(text="X",font=20)
    else:
        tombol4['state'] = DISABLED
        tombol4.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn5():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol5['state'] = DISABLED
        tombol5.config(text="X",font=20)
    else:
        tombol5['state'] = DISABLED
        tombol5.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn6():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol6['state'] = DISABLED
        tombol6.config(text="X",font=20)
    else:
        tombol6['state'] = DISABLED
        tombol6.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn7():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol7['state'] = DISABLED
        tombol7.config(text="X",font=20)
    else:
        tombol7['state'] = DISABLED
        tombol7.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn8():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol8['state'] = DISABLED
        tombol8.config(text="X",font=20)
    else:
        tombol8['state'] = DISABLED
        tombol8.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()
def Buttonn9():
    global jumlahklik
    jumlahklik.set(jumlahklik.get() + 1)
    if jumlahklik.get() % 2:
        # print('lu udah jalan 2 kali')
        tombol9['state'] = DISABLED
        tombol9.config(text="X",font=20)
    else:
        tombol9['state'] = DISABLED
        tombol9.config(text="O",font=20)
    pemenang = checkmenang()
    if pemenang:
        pemenangs.config(text="pemenangnya adalah : " + pemenang)
        disabledall()

# kolom 1
tombol1 = Button(root,text='',height= 5, width=10,command=Buttonn1,state=DISABLED)
tombol1.grid(row=1,column=0,padx=20,pady=20)

tombol2 = Button(root,text='',height= 5, width=10,command=Buttonn2,state=DISABLED)
tombol2.grid(row=1,column=1,padx=20,pady=20)

tombol3 = Button(root,text='',height= 5, width=10,command=Buttonn3,state=DISABLED)
tombol3.grid(row=1,column=2,padx=20,pady=20)

# kolom 2
tombol4 = Button(root,text='',height= 5, width=10,command=Buttonn4,state=DISABLED)
tombol4.grid(row=2,column=0,padx=20,pady=20)

tombol5 = Button(root,text='',height= 5, width=10,command=Buttonn5,state=DISABLED)
tombol5.grid(row=2,column=1,padx=20,pady=20)

tombol6 = Button(root,text='',height= 5, width=10,command=Buttonn6,state=DISABLED)
tombol6.grid(row=2,column=2,padx=20,pady=20)

# kolom 3
tombol7 = Button(root,text='',height= 5, width=10,command=Buttonn7,state=DISABLED)
tombol7.grid(row=3,column=0,padx=20,pady=20)

tombol8 = Button(root,text='',height= 5, width=10,command=Buttonn8,state=DISABLED)
tombol8.grid(row=3,column=1,padx=20,pady=20)

tombol9 = Button(root,text='',height= 5, width=10,command=Buttonn9,state=DISABLED)
tombol9.grid(row=3,column=2,padx=20,pady=20)

# Pesan/Higlight siapa yang menang
pemenangs = Label(root,text='Hasil')
pemenangs.grid(row=4,column=1)
restart_button = Button(root, text="Restart",state=DISABLED,command=Restart)
restart_button.grid(row=4,column=2)

root.mainloop()