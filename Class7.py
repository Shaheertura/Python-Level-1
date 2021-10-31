a=int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

if(a>b and a>c):
    print(a,"is the Greatest")
elif(b>a and b>c):
    print(b,"is the Greatest")
else:
    print(c,"is the Greatest")
