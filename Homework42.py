from tkinter import *
import random 
root=Tk()
root.geometry("500x400")
root.title("Roll Dice")
l=Label(root,text="",font=("times",260))

def roll():
  dice=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
  l.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
  l.pack()
b=Button(root,text="Let's roll....",width=40,height=5,font=10,bg="cadet blue",bd = 2,command=roll)
b.pack(padx=10,pady=10)

root.mainloop()
