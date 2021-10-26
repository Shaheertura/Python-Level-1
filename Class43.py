from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Notepad")
root.geometry('600x600')
root.resizable(False,False)
root.iconbitmap(r'G:\Documents\Downloads\download-_1_.ico')
def Savefile():
    openfile = filedialog.asksaveasfile(mode='w',defaultextension = ".txt")
    if openfile == None:
        return
    text=str(entry.get(1.0,END))
    openfile.write(text)
    openfile.close()

def Openfile():
    file = filedialog.askopenfile(mode='r',filetype = [("Text Files","*.txt")])
    if file != None:
        content = file.read()
        entry.insert(INSERT,content)
    
btn1 = Button(root,text="Save",font=('arial',8,'bold'),width=20,height=2,command=Savefile)
btn1.place(x=100,y=5)

btn2 = Button(root,text="Open",font=('arial',8,'bold'),width=20,height=2,command=Openfile)
btn2.place(x=300,y=5)

entry = Text(root,font=('arial',10,'bold'),height=33,width=72,wrap = WORD)
entry.place(x=10,y=60)

root.mainloop()
