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

#Analog clock
try:
    import tkinter
except:
    import tkinter as tkinter

class main(tkinter.Tk):
    def __init__(self):
        self.x=150
        self.y=150
        self.length=50
        self.creating_all_function_trigger()

    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.creating_background_()
        self.creating_sticks()
        return

    def creating_background_(self):
        self.image=tkinter.PhotoImage(file='name of the file here')
        self.canvas.create_image(150,150, image=self.image)
        return

    def create_canvas_for_shapes(self):
        self.canvas=tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes',fill='both')
        return

    def creating_sticks(self):
        self.sticks=[]
        for i in range(3):
            store=self.canvas.create_line(self.x, self.y, self.x+self.length, self.y+self.length,width=2, fill='red')
            self.sticks.append(store)
        return

    def update_class(self):
        now=time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t ))*5
        now=(hour,now.tm_min,now.tm_sec)

        for n,i in enumerate(now):
            x,y=self.canvas.coords(self.sticks[n])[0:2]
            cr=[x,y]
            cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))
        return

if __name__ == '__main__':
    root=main()

    while True:
        root.update()
        root.update_idletasks()
        root.update_class() 