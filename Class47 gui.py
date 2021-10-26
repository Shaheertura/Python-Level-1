from tkinter import *

root = Tk()
root.geometry('500x500')
root.config(bg='cadet blue')
en1 = Entry(root,font=('arial',20,'bold'),width=8)


en2 = Entry(root,font=('arial',20,'bold'),width=8)

en1.place(x=100,y=100)
en2.place(x=100,y=200)

def calc():
    a = int(en1.get())
    b = int(en2.get())

    c = a + b

    lbl2 = Label(root,bg="cadet blue",width=10,height=10)
    lbl2.place(x=200,y=150)
    lbl = Label(root,text=f'{c}',font=('aria',20,"bold"),bg='cadet blue')
    lbl.place(x=200,y=150)
    

btn1 = Button(root,text="Add",width=8,font=("arial",20,"bold"),command=calc)
btn1.place(x=200,y=400)



root.mainloop()
