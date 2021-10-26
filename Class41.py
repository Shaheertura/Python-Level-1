try:
    from tkinter import *
except:
    print("Modules Cant be imported")
root = Tk()
root.config(bg='cadet blue')
root.title("Management System")
root.geometry("1200x750")
lbl1 = Label(root,text="Bill Management",font=('arial',80,'bold'),bg='cadet blue')
lbl1.place(x=80,y=0)

frame1 = Frame(root,width=400,height=580, relief='ridge',bd=5,bg='light green')
frame1.place(x=0,y=130)


frame2 = Frame(root,width=400,height=580, relief='ridge',bd=5,bg='light green')
frame2.place(x=400,y=130)

frame3 = Frame(root,width=400,height=580, relief='ridge',bd=5,bg='light green')
frame3.place(x=800,y=130)

mtitle = Label(frame1,text="Menu",font=('arial',50,'bold'),bg='light green')
mtitle.place(x=70,y=0)


mlbl1 = Label(frame1,text="Grilled Fish:    19.99",font=('arial',20,'bold'),bg='light green')
mlbl1.place(x=0,y=80)

mlbl2 = Label(frame1,text="Grill Cheese:    15.00",font=('arial',20,'bold'),bg='light green')
mlbl2.place(x=0,y=120)

mlbl3 = Label(frame1,text="French Toast:    10.00",font=('arial',20,'bold'),bg='light green')
mlbl3.place(x=0,y=160)

mlbl4 = Label(frame1,text="Cookies:         19.99",font=('arial',20,'bold'),bg='light green')
mlbl4.place(x=0,y=200)

mlbl5 = Label(frame1,text="Apple Juice:     5.00",font=('arial',20,'bold'),bg='light green')
mlbl5.place(x=0,y=240)

mlbl6 = Label(frame1,text="Orange Juice:    5.00",font=('arial',20,'bold'),bg='light green')
mlbl6.place(x=0,y=280)

mtitle = Label(frame1,text="Menu",font=('arial',50,'bold'),bg='light green')
mtitle.place(x=70,y=0)


lbl1 = Label(frame2,text="Grilled Fish",font=('arial',20,'bold'),bg='light green')
lbl1.place(x=0,y=80)

lbl2 = Label(frame2,text="Grilled Cheese",font=('arial',20,'bold'),bg='light green')
lbl2.place(x=0,y=120)

lbl3 = Label(frame2,text="French Toast",font=('arial',20,'bold'),bg='light green')
lbl3.place(x=0,y=160)

lbl4 = Label(frame2,text="Cookies",font=('arial',20,'bold'),bg='light green')
lbl4.place(x=0,y=200)

lbl5 = Label(frame2,text="Apple Juice",font=('arial',20,'bold'),bg='light green')
lbl5.place(x=0,y=240)

lbl6 = Label(frame2,text="Orange Juice",font=('arial',20,'bold'),bg='light green')
lbl6.place(x=0,y=280)

mtxt1 = Entry(frame2,font=('arial',20,'bold'),width=8)
mtxt1.place(x=200,y=80)

mtxt2 = Entry(frame2,font=('arial',20,'bold'),width=8)
mtxt2.place(x=200,y=120)

mtxt3 = Entry(frame2,font=('arial',20,'bold'),width=8)
mtxt3.place(x=200,y=160)

mtxt4 = Entry(frame2,font=('arial',20,'bold'),width=8)
mtxt4.place(x=200,y=200)

mtxt5 = Entry(frame2,font=('arial',20,'bold'),width=8)
mtxt5.place(x=200,y=240)

mtxt6 = Entry(frame2,font=('arial',20,'bold'),width=8)
mtxt6.place(x=200,y=280)

def Calculate():
    gf = int(mtxt1.get())
    gc = int(mtxt2.get())
    ft = int(mtxt3.get())
    c = int(mtxt4.get())
    aj = int(mtxt5.get())
    oj = int(mtxt6.get())
    c = c = 20
    aj = aj * 5
    oj = oj * 5

    gf = gf * 20

    gc = gc * 15

    ft = ft * 10

    total = gf + gc + ft + c + aj + oj

    

    amount = Label(frame3,text=f"""
Grilled Fish {gf}

Grilled Cheese {gc}

French Toast{ft}

Cookies{c}

Applie Juice {aj}

Ornage Juice{oj}

The Total is {total}
""",font=('arial',20,'bold'),bg='light green')
    amount.place(x=50,y=50)

    
    

calc = Button(frame3,font=('arial',20,'bold'),width=8,text="Calculate",bg='cadet blue',command=Calculate)
calc.place(x=100,y=450)







root.mainloop()
