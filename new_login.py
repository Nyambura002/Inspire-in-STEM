from tkinter import *
root = Tk()
root.title("STUDENT INFORMATION BY @Nyambura :)")
root.minsize(height=300,width=300)
root.configure(bg='grey')



def tab1():
    def tab2():
        label1.destroy()
        button1.destroy()
        label2=Label(root,text='INFO TAB',font=('TIMES_NEW_ROMAN',28))
        label2.pack()
        def back():
            label2.destroy()
            button2.destroy()
            tab1()
        button2=Button(root,text='BACK',font=('TIMES_NEW_ROMAN',28),command=back)
        button2.pack(side=BOTTOM)
    label1=Label(root,text='REGISTRATION TAB',font=('TIMES_NEW_ROMAN',28))
    label1.pack()
    f_name = Label(root, text="First Name:", font=("Lucida Calligraphy", 20), bg='turquoise')
    f_name.pack()
    s_name = Label(root, text="Second Name:", font=("Lucida Calligraphy", 20),bg='turquoise')
    s_name.pack()
    
    
    f_name_box = Entry(root, width=30)
    f_name_box.pack()

    s_name_box = Entry(root, width=30)
    f_name_box.pack()


    button1=Button(root,text='SUBMIT',font=('TIMES_NEW_ROMAN',28),command=tab2)
    button1.pack(side=BOTTOM)

    f_name = Label(root, text="First Name:", font=("Lucida Calligraphy", 20), bg='turquoise')

tab1()
root.mainloop()
