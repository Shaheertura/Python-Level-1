#odd num1bers
for w in range(1,2):
    a = int(input("Enter a num1ber to Start from: "))
    q = int(input("Enter the num1ber to end from: "))
    for i in range(a,q):
        if i % 2 != 0:
            print(i)


num1 = int(input("Enter any num1ber: "))
temp = num1
rev = 0
while(num1>0):
    dig=num1%10
    rev=(rev*10)+dig
    num1=num1//10
if(temp==rev):
    print("Palindrome num1ber ")
else:
    print("Not Palindrome num1ber ")


num1 = int(input("Enter a number: "))    
factorial = 1    
if num1 < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num1 == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num1 + 1):    
       factorial = factorial*i    
   print("The factorial of",num1,"is",factorial) 



c = int(input("Enter a Number to Multiply: "))

for z in range(1,11):
    if z % 2 != 0:
        print(c, "X",z,"=",(c*z))
    else:
        pass






