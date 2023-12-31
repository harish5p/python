# import
from tkinter import *


# GUI interaction
window = Tk()
window.geometry('500x500')

# Inputs

# Entry Box
e = Entry(window, width=56,  borderwidth=5  )
e.place(x=0, y=0)

# Buttons


def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))
    
WIDTH = 5


b = Button(window, text='1', width=WIDTH, command=lambda: click(1))
b.place(x=10, y=60)

b = Button(window, text='2', width=WIDTH, command=lambda: click(2))
b.place(x=90, y=60)

b = Button(window, text='3', width=WIDTH, command=lambda: click(3))
b.place(x=170, y=60)

b = Button(window, text='4', width=WIDTH, command=lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text='5', width=WIDTH, command=lambda: click(5))
b.place(x=90, y=120)

b = Button(window, text='6', width=WIDTH, command=lambda: click(6))
b.place(x=170, y=120)

b = Button(window, text='7', width=WIDTH, command=lambda: click(7))
b.place(x=10, y=180)

b = Button(window, text='8', width=WIDTH,  command=lambda: click(8))
b.place(x=90, y=180)

b = Button(window, text='9', width=WIDTH, command=lambda: click(9))
b.place(x=170, y=180)

b = Button(window, text='0', width=WIDTH, command=lambda: click(0))
b.place(x=10, y=240)

# OPERATORS


def add():
    n1 = e.get()
    global oper
    oper = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text='+', width=WIDTH, command=add)
b.place(x=90, y=240)


def subt():
    n1 = e.get()
    global oper
    oper = 'subtraction'
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text='-', width=WIDTH, command=subt)
b.place(x=170, y=240)


def mult():
    n1 = e.get()
    global oper
    oper = 'multiplication'
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text='*', width=WIDTH, command=mult)
b.place(x=10, y=300)


def divi():
    n1 = e.get()
    global oper
    oper = 'division'
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window, text='/', width=WIDTH, command=divi)
b.place(x=90, y=300)


def equalto():
    n2 = e.get()
    e.delete(0, END)
    if oper == "addition":
        e.insert(0, i + int(n2))
    elif oper == "subtraction":
        e.insert(0, i - int(n2))
    elif oper == "multiplication":
        e.insert(0, i * int(n2))
    elif oper == "division":
        e.insert(0, i / int(n2))


b = Button(window, text='=', width=WIDTH, command=equalto)
b.place(x=170, y=300)


def clear():
    e.delete(0, END)


b = Button(window, text='clear', width=WIDTH, command=clear)
b.place(x=10, y=350)

# mainloop
mainloop()
