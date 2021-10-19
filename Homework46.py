from tkinter import *

root = Tk()
root.config(bg='cadet blue')
root.geometry('800x600')

en = Entry(root,font=('arial',20,'bold'))
en.place(x=200,y=100)
"""
def Calc():
    e1 = int(en.get())
    if(e1%2) == 0:
        print(e1,"is a Even Number")
    else:
        print(e1,'is a Odd Number')
    
calc = Button(root,text='Calculate',font=('arial',20,'bold'),command=Calc)
calc.place(x=300,y=200)


def Calc():
    num = int(en.get())
    temp=num
    #Creates a Temporary Variable
    rev=0
    #we Set a variable called rev to 0
    while(num>0):
        # while the number is greater then 0
        dig=num%10
        #we say dig = num % 10 meaning we get the last digit of the number
        rev=rev*10+dig
        #rev multiply rev is 0 + dig which is the last digit
        num=num//10
        #then we divide it by 10 so everything is back to normal
        #then this step loops again and again till num is equal to 0
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
    # is the temp variable which is the number u saved == the reverse also known as rev
    #if it equal together it prints The Number is palaindrome
    #otherwise it prints Not a plaindrome
    

en = Entry(root,font=('arial',20,'bold'))
en.place(x=200,y=100)

calc = Button(root,text='Calculate',font=('arial',20,'bold'),command=Calc)
calc.place(x=300,y=200)


def Calc():
    num = int(en.get())
    #Insitizalize Sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    # display the result
    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")

en = Entry(root,font=('arial',20,'bold'))
en.place(x=200,y=100)

calc = Button(root,text='Calculate',font=('arial',20,'bold'),command=Calc)
calc.place(x=300,y=200)
"""
root.mainloop()
