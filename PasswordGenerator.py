from tkinter import *
from tkinter.ttk import *
import random
import pyperclip

win = Tk()

low = "abcdefghijklmnopqrstuvwxyz"
medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_?"

def Copy():
    global password
    pyperclip.copy(password)

def randomize():
    global password, c, PsEnt
    password = ""
    cmblen = combo.get()
    length = int(cmblen)
    if rb.get() == "Weak":
        for i in range(0,length,1):
            c = random.choice(low)
            password = password+c
    elif rb.get() == "Moderate":
        for i in range(0,length,1):
            c = random.choice(medium)
            password = password+c
    elif rb.get() == "Strong":
        for i in range(0,length,1):
            c = random.choice(strong)
            password = password+c
    PsEnt.delete(0, END)
    PsEnt.insert(0, password)

rb = StringVar()

Pslbl = Label(win,text="Password:",font=('Arial',18))
Pslbl.grid(row=0,column=0)

PsEnt = Entry(win,state='insert')
PsEnt.grid(row=0,column=1)

Lelbl = Label(win,text="Length:",font=('Arial',18))
Lelbl.grid(row=1,column=0)

PsEnclbl = Label(win,text="Password(Encrypted):",font=('Arial',18))
PsEnclbl.grid(row=2,column=0)

PsEncEnt = Entry(win,state='insert')
PsEncEnt.grid(row=2,column=1)

GenBtn = Button(win,text="Generate",command=randomize)
GenBtn.grid(row=0,column=2)

CopyBtn = Button(win,text="Copy",command = Copy)
CopyBtn.grid(row=0,column=3)

combo = Combobox(win)
combo ['values'] = (8,12,16,20,24,28,32,36)
combo.current(0)
combo.grid(row=1,column=1)

Weakrb = Radiobutton(win,text="Weak",value='Weak',var=rb)
Weakrb.grid(row=1,column=2)
Modrb = Radiobutton(win,text="Moderate",value='Moderate',var=rb)
Modrb.grid(row=1,column=3)
Strb = Radiobutton(win,text="Strong",value='Strong',var=rb)
Strb.grid(row=1,column=4)

win.geometry('600x150')
win.mainloop()