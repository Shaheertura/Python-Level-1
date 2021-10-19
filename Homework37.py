from tkinter import *
import tkinter.messagebox

root = Tk()

root.geometry("500x400+0+0")
root.title("Simple Intrest Calculator")
root.config(bg='cadet blue')



prin = Label(root,text="Principal",font=('arial',20,'bold'),width=8)
prin.place(x=50,y=20)

Principal = StringVar()

eprin = Entry(root,textvariable=Principal, font=('arial',20,'bold'),width=8) 
eprin.place(x=200,y=20)


Rate = StringVar()

rate = Label(root,text="Rate",font=('arial',20,'bold'),width=8)
rate.place(x=50,y=90)

erate = Entry(root,font=('arial',20,'bold'),textvariable=Rate,width=8)
erate.place(x=200,y=90)

Time = StringVar()



time = Label(root,text="Time",font=('arial',20,'bold'),width=8)
time.place(x=50,y=160)

etime = Entry(root,font=('arial',20,'bold'),textvariable=Time,width=8)
etime.place(x=200,y=160)



def Calculate():
    a = int(eprin.get())
    b = int(erate.get())
    c = int(etime.get())


    amount = (a * c * b) / 100
    Label(text=f"{amount}",font="arial 30 bold",bg="cadet blue").place(x=200,y=220)



    

    
btn1 = Button(root,font=('arial',20,'bold'),text="Calculate",bg="cadet blue",command=Calculate)
btn1.place(x=120,y=280)

btn2 = Button(root,font=('arial',20,'bold'),text="Exit", bg="cadet Blue",command=lambda:exit())





root.mainloop()
