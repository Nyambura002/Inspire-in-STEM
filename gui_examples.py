#!/usr/bin/python

#################################################################################################
#                             Name : Faith Njuguna
#                             Date : 7/06/2022
#                             gui_examples using ktinker
#################################################################################################

from tkinter import *

window = Tk()
window.title("Welcome to my App!")
window.configure(bg='turquoise') #Change background colour

window.geometry("400x400") 

f_name = Label(window, text="First Name:", font=("Lucida Calligraphy", 20), bg='turquoise')
s_name = Label(window, text="Second Name:", font=("Lucida Calligraphy", 20),bg='turquoise')

f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)


def open_popup():
    top = Toplevel(window)
    top.geometry("300*300")
    top.title("Pop Up")
    top.configure(bg='purple')
    msg = Label(top,text = "Welcome to this new window", font=("Arial", 28), command = open_popup().pack())

btn = Button(window, text = "Sign up", bg="grey",fg="white")
btn.grid(column = 100, row = 180)

f_name_box = Entry(window , width=30)
f_name_box.grid(column = 100, row = 100)


s_name_box = Entry(window , width=30)
s_name_box.grid(column = 100 , row = 120)

window.mainloop()


