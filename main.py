#this will be the main file to run the project.

from tkinter import *
from caesar_cipher import Caesar_Cipher_E, Caesar_Cipher_D
from playfair_cipher import Playfair_Cipher_E, Playfair_Cipher_D
from columnar_cipher import columnar_encrypt, columnar_decrypt


def Choose_Algorthim_E():
    if var.get() == 1:
        output = Caesar_Cipher_E(var2.get(), int(var1.get()))
        var3.set(output)
    elif var.get() == 2:
        output = Playfair_Cipher_E(var2.get(), var1.get())
        var3.set(output)
    elif var.get() == 3:
        output = columnar_encrypt(var2.get(), int(var1.get()))
        var3.set(output)
    else:
        print("error")


def Choose_Algorthim_D():
    if var.get() == 1:
        output = Caesar_Cipher_D(var3.get(), int(var1.get()))
        var2.set(output)
    elif var.get() == 2:
        output = Playfair_Cipher_D(var3.get(), var1.get())
        var2.set(output)
    elif var.get() == 3:
        output = columnar_decrypt(var3.get(), int(var1.get()))
        var2.set(output)
    else:
        print("error")


def Reset():
    var1.set('0')
    var2.set('')
    var3.set('')


window = Tk()
window.geometry('320x450+250+250')  # size & appearance place
window.title('Encryption & Decryption Algorithms')
Label(text="Encryption & Decryption Algorithms", fg='black', bg='white').place(x=60, y=0)

var = IntVar()
var.set(1)
Label(text="Choose Your Algorithm:", fg='black', bg='white').place(x=0, y=30)
Radiobutton(window, text="Caesar Cipher", variable=var, value=1).place(x=0, y=55)
Radiobutton(window, text="Play Fair", variable=var, value=2).place(x=0, y=75)
Radiobutton(window, text="Columnar", variable=var, value=3).place(x=0, y=95)

var1 = StringVar()
var1.set('0')
Label(text="Enter The Key", fg='black').place(x=110, y=120)
Entry(window, justify=CENTER, width=30, textvariable=var1).place(x=70, y=140)

var2 = StringVar()
Label(text="Enter Text To Encrypt", fg='black').place(x=90, y=180)
Entry(window, justify=CENTER, width=50, textvariable=var2).place(x=5, y=200)
Button(text="Encryption", bg='white', command=Choose_Algorthim_E).place(x=120, y=220)

var3 = StringVar()
Label(text="Encrypted Text", fg='black').place(x=110, y=270)
Button(text="Decryption", bg='white', command=Choose_Algorthim_D).place(x=115, y=310)
Entry(window, justify=CENTER, width=50, textvariable=var3).place(x=5, y=290)
Button(text="Reset", bg='white', command=Reset).place(x=278, y=422)
window.mainloop()


