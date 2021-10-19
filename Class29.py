from tkinter import *
root = Tk()
root.config(bg='cadet blue')
root.title("Weight Caclulator")
root.geometry('700x500+0+0')

title = Label(root, text="Weight Calculator", font=('arial',50,'bold'),bg='cadet blue')
title.place(x=70,y=0)



lbl1 = Label(root,text='Kg',font=('arial',40,'bold'), bg='cadet blue')
lbl1.place(x=130,y=150)

txt1 = Entry(root,font=('arial',40,'bold'),width=15)
txt1.place(x=210,y=150)




def Calculate():
    a = float(txt1.get())

    kgg = a*1000

    kgp = a*2.2046

    kgo = a*35.274


    clbl1 = Label(root,text=f"Grams: {kgg}",font=('arial',25,'bold'),bg='cadet blue')
    clbl1.place(x=180,y=260)

    clbl2 = Label(root,text=f"Pounds: {kgp}",font=('arial',25,'bold'),bg='cadet blue')
    clbl2.place(x=180,y=220)

    clbl3 = Label(root,text=f"Ounce: {kgp}",font=('arial',25,'bold'),bg='cadet blue')
    clbl3.place(x=180,y=300)
    


    
btn1 = Button(root,text="Calculate",width=15,bg='cadet blue', font=('arial',40,'bold'),command=Calculate)
btn1.place(x=180,y=380)
root.mainloop()
