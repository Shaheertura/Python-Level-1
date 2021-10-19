
p=int(input("Enter a Number: "))
for h in range(p+1,0,-1):
    for j in range(0,p,-1):
        print("*", end='')
    print(" ")







n=int(input("Enter any Number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
