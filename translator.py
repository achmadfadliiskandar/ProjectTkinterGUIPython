from tkinter import *
from tkinter import ttk,messagebox
from deep_translator import GoogleTranslator
import googletrans

root = Tk()
root.geometry('550x200')
root.title("APLIKASI TERJEMAH BASIS DESKTOP")

judul = Label(root,text="APLIKASI TRANSLATOR",font=("Arial",27,'bold'))
judul.pack()

inputan = Entry(root,bg='orange',fg='black',width=100)
inputan.pack(side="top", fill="x")

# Mendapatkan daftar kode bahasa dari googletrans.LANGCODES
lang_codes = list(googletrans.LANGCODES.keys())

# MENDEFINISIKAN SELURUH DATA YANG AKAN DIBENTUK MENJADI COMBOBOX ADALAH STRING
n = StringVar()

kodebahasa = ttk.Combobox(root, textvariable=n, state='readonly')
kodebahasa['values'] = lang_codes

for i, lang in enumerate(lang_codes):
    kodebahasa.current(i)
    kodebahasa.pack()   
kodebahasa.pack(side="top", fill="x")

def Translate():
    getkb = kodebahasa.get()
    input_text = inputan.get()
    if not input_text:
        messagebox.showerror('Error', 'Please enter text to translate.')
    else:
        try:
            translation = GoogleTranslator(source='auto', target=getkb).translate(input_text)
            hasilinputan.config(text=translation)
            # print(getkb)
        except Exception as e:
            messagebox.showerror('Error', str(e))

tombolsub = Button(root,text='Terjemahkan',command=Translate)
tombolsub.pack(side="top", fill="x")

hasilinputan = Label(root,text="Keterangan : menunggu terjemahan")
hasilinputan.pack()

root.mainloop()