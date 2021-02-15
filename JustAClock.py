from tkinter import *
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title("Just A Clock")


def time():
    txt = strftime("%H:%M:%S")
    label.config(text=txt)
    label.after(1000, time)


label = Label(root, font=('ds-digital', 80),
              background="black", foreground="white")
label.pack(anchor='center')
time()
mainloop()
