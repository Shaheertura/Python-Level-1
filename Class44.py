from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("File Exploler")
root.geometry("500x500")
root.config(bg='cadet blue')
def Openfile():
    file = filedialog.askopenfile(mode='r',filetype = [("Text Files","*.*")])
    if file != None:
        content = file.read()
        entry.insert(INSERT,content)
        
def Browsefile():
    filename = filedialog.askopenfilename(initialdir="/",title="select a file",filetypes=(("Text Files","*.txt"),
                                                                                          ("All Files","*.*")))
    labelfileexplorer.configure(text="File Opened"+filename)
entry = Text(root,font=('arial',10,'bold'),height=33,width=72,wrap = WORD)
entry.place(x=600,y=200)

lbl1 = Label(root,text="File Explorer",font=('arial',20,'bold'),bg = 'cadet blue',width=100,height=4)
lbl1.grid(row=1,column=1)
    
btn1 = Button(root,text="Browse File",command=Browsefile)
btn1.grid(row=2,column=1)

opnbtn = Button(root,text="Open",command=Openfile)
opnbtn.place(x=834,y=100)
def iExit():
    iExit = messagebox.askyesno("File Explorer", "Confirm if you want to Exit")
    if iExit > 0:
        root.destroy()
extbtn = Button(root,text="Exit",command=iExit)
extbtn.grid(row=3,column=1)
root.mainloop()
