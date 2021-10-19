from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("ToDo App")
root.geometry('300x400')
root.config(bg='light green')
root.resizable(False,False)

def iExit():
    Exit = messagebox.askyesno("ToDo App", "Confirm if you want to Exit")

    if Exit > 0:
        root.destroy()


def ToDo():
    data = txt1.get()
    
    
    
    entry.insert(INSERT,f"[ {i} ]{data}\n")

    tasklist.append(data)
    counter+=1



    
lbl1 = Label(root,text="Enter Your Task", font=('arial',10),bg='light green')
lbl1.place(x=100,y=0)

txt1 = Entry(root,font=('arial',10))
txt1.place(x=75,y=30)

btn1 = Button(root,text='Submit',bg='red', font=('arial',10,'bold'),command=ToDo)
btn1.place(x=115,y=50)

entry = Text(root,font=('arial',10,'bold'),height=10,width=40)
entry.place(x=6,y=80)

btn2 = Button(root,text="Delete Task Number",bg='blue',font=('arial',10,'bold'))
btn2.place(x=75,y=250)

txt2 = Entry(root,font=('arial',10),width=3)
txt2.place(x=130,y=280)

btn3 = Button(root,text="Delete",bg='red',font=('arial',10,'bold'))
btn3.place(x=115,y=305)

btn4 = Button(root,text="Exit",bg='red',font=('arial',10,'bold'),command=iExit)
btn4.place(x=122,y=335)
root.mainloop()
