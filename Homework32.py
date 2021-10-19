from tkinter import *
root = Tk()

def func():
    print("Text\n")

def func2():
    for x in range(1,4):        
        print(f"Text {x}\n")

def func3():
    print("""
Test Paragraph
This is Paragraph This is Paragraph
This is Paragraph
This is Paragraph
This is Paragraph This is Paragraph
\n
""")

def func4():
    for x in range(1,11):
        
        print("""
    Test Paragraph 
    This is Paragraph This is Paragraph
    This is Paragraph
    This is Paragraph
    This is Paragraph This is Paragraph
    \n
    """)
btn = Button(root,text="Button 1",command=func).pack()

btn2 = Button(root,text="Button 2",command=func2).pack()

btn3 = Button(root,text="Button 3",command=func3).pack()

btn4 = Button(root,text="Button 4",command=func4).pack()
root.mainloop()
