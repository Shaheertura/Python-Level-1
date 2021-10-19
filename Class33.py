"""
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side=LEFT)
root.mainloop()
"""


from tkinter import *
root = Tk()
frame1 = Frame(root).pack()
bottomframe = Frame(root).pack(side=BOTTOM)
bluebutton = Button(frame1, text="Blue", fg="blue").pack(side=RIGHT)
yellbutton = Button(frame1, text="Yellow",fg="yellow").pack()
redbutton = Button(frame1, text="Red", fg="red").pack(side=LEFT)
blackbutton = Button(bottomframe, text="Black", fg="black").pack()

