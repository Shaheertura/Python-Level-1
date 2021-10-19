'''
from tkinter import *

root = Tk()

def dis():
    print("This is a Printed Message")

btn1 = Button(root,text="Click me", command=dis)

btn1.pack()


root.mainloop()
'''
from tkinter import *
root = Tk()

frame1 = Frame(root, width=800,height=500, relief='ridge',bg='cadet blue', bd=20)
frame1.grid(row=0,column=0)

txt1 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt1.grid(row=0,column=0)

txt2 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt2.grid(row=0,column=1)

txt3 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt3.grid(row=0,column=2)


txt4 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt4.grid(row=1,column=0)

txt5 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt5.grid(row=1,column=1)

txt6 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt6.grid(row=1,column=2)

txt7 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt7.grid(row=2,column=0)

txt8 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt8.grid(row=2,column=1)

txt9 = Entry(frame1,font=('arial',20,'bold'),width='10')
txt9.grid(row=2,column=2)
root.mainloop()
