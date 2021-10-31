'''
i=1
sum = 0
while(i<=15):
    if(i%2!=0):
        sum=sum+i
    i+=1
print(sum)

n=int(input("Enter any Number: "))
for i in range(1,11):
    print(n,"X",i,"=",(n*i))


Nested Loops

a=["red","blue","green","yellow"]
fruits=["apple","banana","cherry"]

for iterating_var in sequence:
    for iterating_var in sequence:
        statment(s)

    statement(s)

for i in a:
    for y in fruits:
        print(i,y)

while(expresstion):
    while(expresstion):
        statement(s)
    statement(s)

i=1

while(i<=3):
    print(i,"Outer Loop is executed only once")
    j=1
    while(j<=3):
        print(j,"Inner Loop is executed until Completion")
        j+=1
    i+=1

for loops if else:

n = int(input("Enter a number: "))
for i in range(1,11):
    if(n==0):
        print("Not a valid Number")
    else:
        print(n*i)'''

    





















