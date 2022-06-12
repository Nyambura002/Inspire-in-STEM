#!/usr/bin/python


#################################################################################################
#                             Name : Faith Njuguna
#                             Date : 8/06/2022
#                             CLOCK ASSIGNMENT
#################################################################################################

import tkinter as ui
import time
import math

window = ui.Tk()

window.title("Simple Clock by @Nyambura :)") 

#Digital clock
def update_clock():
    hours = time.strftime("%I")   #current hour in 12 hr system
    minutes = time.strftime("%M") #formating current minute
    seconds= time.strftime("%S") #current seconds
    am_or_pm = time.strftime("%p") #am or pm
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    clock_lbl.config(text = time_text)
    clock_lbl.after(1000, update_clock) #the update_clock function will be called each second

clock_lbl = ui.Label(window, text="00:00:00", font="Helvetica 72 bold")
clock_lbl.pack()

update_clock()

window.mainloop() #keeps the window open

 
        