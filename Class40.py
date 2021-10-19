#-------Modules and libs--------#
from datetime import date       #
from tkinter import *           #
from tkinter import messagebox  #
#-------------------------------#
root = Tk()
root.geometry('1350x750')
root.config(bg='cadet blue')
root.title('Age Calculator')
root.iconbitmap(r'G:\Documents\Downloads\Age.ico')
w = Label(root,text="Age Calculator",font=('arial',90,'bold'),bg='cadet blue')
w.place(x=350,y=0)

dobl1 = Label(root,text="Day",font=('arial',30,'bold'),bg='cadet blue')
dobl1.place(x=100,y=200)
dobe1 = Entry(root,font=('arial',30,'bold'))
dobe1.place(x=200,y=200)

dobl2 = Label(root,text="Month",font=('arial',30,'bold'),bg='cadet blue')
dobl2.place(x=70,y=300)
dobe2 = Entry(root,font=('arial',30,'bold'))
dobe2.place(x=200,y=300)

dobl3 = Label(root,text="Year",font=('arial',30,'bold'),bg='cadet blue')
dobl3.place(x=100,y=400)
dobe3 = Entry(root,font=('arial',30,'bold'))
dobe3.place(x=200,y=400)

#--------------------------------------------------------------------------------
    
doblr1 = Label(root,text="Day",font=('arial',30,'bold'),bg='cadet blue')
doblr1.place(x=750,y=200)
dober1 = Entry(root,font=('arial',30,'bold'))
dober1.place(x=850,y=200)

doblr2 = Label(root,text="Month",font=('arial',30,'bold'),bg='cadet blue')
doblr2.place(x=727,y=300)
dober2 = Entry(root,font=('arial',30,'bold'))
dober2.place(x=850,y=300)

doblr3 = Label(root,text="Year",font=('arial',30,'bold'),bg='cadet blue')
doblr3.place(x=750,y=400)
dober3 = Entry(root,font=('arial',30,'bold'))
dober3.place(x=850,y=400)
#----------------------------------Button-------------------------------------------------
def Calculate():
    Day = dobe1.get()
    Month = dobe2.get()
    Year = dobe3.get()


    today = date.today()
    print(today)

    dob = date(int(Year),int(Month),int(Day))

    agey = today.year - dob.Year
    agem = today.month - dob.Month
    aged = today.day - dob.Day

    dober1.set(aged)
    dober2.set(agem)
    dober3.set(agey)
    

    

    
    
    
calc = Button(root,text="Calculate",font=('arial',30,'bold'),bg='cadet blue',width=8,command=Calculate)
calc.place(x=500,y=500)
    
root.mainloop()
