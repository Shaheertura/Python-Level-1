from random import randint
import sys

print("Rounds Max Rounds 1-100")

rounds = int(input("Enter the Amount of rounds: "))
print()

for x in range(1,rounds+1):
    print("Round:",x)
    print()
    first = int(input("Enter Your Number: "))
    for i in range(1,100):
        print()
    t = True
    while t == True:
        second = int(input("Enter Your Number to Guess: "))
        print()
        if second == first:
            t = False
            print("You Won Congratulations :)\n")
        else:
            t = True
            print("Wrong Try Again\n")
            

            
                     
    

