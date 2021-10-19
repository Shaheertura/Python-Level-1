import time
def banner():
    print("""
 _____ _           _                    
/  ___| |         | |                   
\ `--.| |__   __ _| |__   ___  ___ _ __ 
 `--. \ '_ \ / _` | '_ \ / _ \/ _ \ '__|
/\__/ / | | | (_| | | | |  __/  __/ |   
\____/|_| |_|\__,_|_| |_|\___|\___|_|   
                                        
                                        
    
    """)
banner()
#si=(p*r*t)/100
def si():
    p = int(input("Enter the Principle: "))
    r = int(input("Enter the Rate: "))
    t = int(input("Enter the Time: "))
    si=(p*r*t)/100
    print(si)

def set1():
    set1 = {345,234,725}
    for x in set1:
        print(x)


def records():
    record1 = input("Enter Your Record: ")
    record2 = input("Enter Your Record: ")
    record3 = input("Enter Your Record: ")
    record4 = input("Enter Your Record: ")
    record5 = input("Enter Your Record: ")
    blankset = {record1,record2,record3,record4,record5}
    print(blankset)

def palendrome():
    pal = int(input("Enter a Number: "))
    cop = pal
    rev = 0
    while (pal>0):
        dig = pal%10
        rev=rev*10+dig
        pal = pal//10
    if cop == rev:
        print("Palendrome")
    else:
        print("Not Palendrome")

num1 = int(input("Enter a Number: "))
def prime(num1):
    
    factor = 1
    count = 0
    while factor<=num1:
        if num1%factor==0:
            count += 1
        factor += 1
    return count
p = prime(num1)
if p == 2:
    print("Prime!")
else:
    print("Not Prime :(")

















