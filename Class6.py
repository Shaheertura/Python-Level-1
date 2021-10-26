'''num = int(input("Enter a number: "))
if ((num%2==0) and (num>100)):
    print("Even!")
else:
    print("Odd!")'''

grade = input("Enter Your Grade: ")
if(grade=='A'):
    print("You Scored 80-90%")
elif(grade=='B'):
    print("Your Scored 60-80%")
elif(grade=='C'):
    print("You Scored 40-60%")
elif(grade='D'):
    print("You Failed in the Examination")
else:
    print("Invalid Grade")

a = int(input("Enter the first Number: "))
b = int(input("Enter the Secong Number: "))
c = int(input("Enter 1 for Addition\n Enter 2 For Subtraction\n Enter 3 for Product\n Enter 4 for Division\n Enter 5 for Remainder"))

if (c==1):
    print("Sum: ",a+b)
elif(c==2):
    print("Diffrence: ",a-b)
elif(c==3):
    print("Product: ",a*b)
elif(c==4):
    print("Quotient: ",a/b)
elif(c==5):
    print("Remainder: ",a%b)
else:
    print("Invalid Choice")
    
