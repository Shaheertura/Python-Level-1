from tkinter import *
root = Tk()
root.config(bg='cadet blue')
root.geometry('700x300+0+0')

title = Label(root,text="Grade Calculator",font=('arial',40,'bold'),bg='cadet blue')
title.place(x=150,y=0)

lbl1 = Label(root,text="Grade", font=('arial',20,'bold'), bg='cadet blue')
lbl1.place(x=100,y=80)

txt1 = Entry(root,font=('arial',20,'bold'),width=20)
txt1.place(x=200,y=80)

def Calculate():
    a = int(txt1.get())
    if a > 100:
        amount="Invalid"
    elif a == 100:
        amount = "A+"
    elif a > 94:
        amount = "A"
    elif a > 90:
        amount = "A-"
    elif a > 87:
        amount = "B+"
    elif a > 83:
        amount = "B"
    elif a > 77:
        amount = "B-"
    elif a > 73:
        amount = "C+"
    elif a > 70:
        amount = "C"
    elif a > 67:
        amount = "D+"
    elif a > 59:
        amount = "D"
    elif a > 0:
        amount = "F"    
    lbl2 = Label(root,text=f"{amount}",bg='cadet blue', font=('arial',20,'bold'))
    lbl2.place(x=300,y=130)
        
btn1 = Button(root, text="Calculate",width=15,bg='cadet blue', font=('arial',20,'bold'),command=Calculate)
btn1.place(x=200,y=180)


root.mainloop()
