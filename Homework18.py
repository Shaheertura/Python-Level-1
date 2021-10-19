from math import floor
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

def evenodd():
    find = int(input("Enter a Number: "))
    if find%2==0:
        print(find,"Is Even")
    else:
        print(find,"is Odd")
evenodd()

def fig():
    fig = int(input("Enter a Number: "))
    if fig <= 0:
        print(fig,"is Negetive")
    elif fig >= 0:
        print(fig,"is Positive")
fig()           
    

def comp():
    comp = 400
    print(comp)
    comp2 = 400/550*100
    print(comp2)
comp()
def ask():
    global a1
    global a2
    a1 = int(input("Enter a Number to Add: "))
    a2 = int(input("Enter Your Second Number to Add: "))
ask()
def add():
    a3 = a2 + a1
    print(a3)
add()
