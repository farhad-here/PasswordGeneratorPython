from random import sample as sam
from tkinter import *
from subprocess import getoutput

window = Tk()
window.title("PK")
la = Label(window)
def password():
    len_password = int(e.get())
    capacity = 'qw+=-?/\.><ertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%&*'
    p = ''.join(sam(capacity, len_password))
    la.config(text=p)
    la.pack()
    print(getoutput(f'powershell set-clipboard "{p}"'))

e = Entry(window, bg="orange", bd=12,fg="darkgreen")
e.pack(fill='x')
b = Button(window, text="make",fg = "black",bg= "red",bd='12', command=password)
b.pack(fill='x')

window.geometry("400x300")
window.mainloop()
