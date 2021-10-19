
def banner():
    print("""
 _____ _           _                    
/  ___| |         | |                   
\ `--.| |__   __ _| |__   ___  ___ _ __ 
 `--. \ '_ \ / _` | '_ \ / _ \/ _ \ '__|   Made in UAE
/\__/ / | | | (_| | | | |  __/  __/ |   
\____/|_| |_|\__,_|_| |_|\___|\___|_|   
                                        
                                        
    
    """)
banner()

def numbers():
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    num3 = int(input("Enter the Third Number: "))
    if num1 > num2 and num1 > num3:
        print(num1,"Is Biggest")
    elif num2 > num1 and num2 > num3:
        print(num2,"Is Biggest")
    else:
        print(num3,"Is Greatest")
numbers()       

def reverse():
    rev = input("Enter Number to Reverse: ")
    print(rev[::-1])
reverse()
