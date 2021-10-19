#Test
import math
'''
print("1-Adittion\n2-Subtraction\n3-Multiplication\n4-Division")
user = int(input("Choose 1-4 what to do: "))

if user == 1:
      add1 = int(input("Enter First Number to add: "))
      add2 = int(input("Enter Second Number to add: "))
      add3 = add1+add2
      print("The Sum is",add3)
elif user == 2:
    sub1 = int(input("Enter first Number to subtract: "))
    sub2 = int(input("Enter Second Number to Subtract: "))
    diffrence = sub1 - sub2
    print("The Diffrence is",diffrence)
elif user == 3:
    fac1 = int(input("Enter First number to Multiply: "))
    fac2 = int(input("Enter second Number to Multiply: "))
    product = fac1 * fac2
    print("The Factor is",product)
elif user == 4:
    dividend = int(input("Enter first Number to divide: "))
    divisor = int(input("Enter second number to divide: "))
    answer = dividend / divisor
    print("The Answer is", answer)
else:
    print("Invalid")
'''
'''
print("1-Square root\n2-Cube Root")
choice = int(input("Enter 1-2: "))
if choice == 1:
    usersq = int(input("Enter number to Find the Square root: "))
    sq = math.sqrt(usersq)
    if ((sq*sq)==usersq):
        print(sq,"Perfect Match")
    else:
        print("Not a Match ")
if choice == 2:
    usercube = int(input("Enter a Number to find cube root: "))
    answer = usercube**(1/3)
    print(answer)
'''
print("1-Simple Intrest\n2-Compund Intrest")
choose = int(input("Enter 1-2: "))
if choose == 1:
    p = int(input("Enter the Principle: "))
    r = int(input("Enter the Rate: "))
    t = int(input("Enter the time: "))
    si = (p*r*t)/100
    print(si)
elif choose == 2:
    a = int(input("Enter the Amount: "))
    p = int(input("Enter the Principal: "))
    r = int(input("Enter the Rate: "))
    n = int(input("Enter the Number of times intrest applied per time period: "))
    t = int(input("Enter Number of time Periods Elasped: "))
    ci = p * (((1 + ((r/100.0)/n)) ** (n*t)))
    print(ci)
    
            
        
