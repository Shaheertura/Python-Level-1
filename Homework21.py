
lis = []
for x in range(2,101):
    f=0
    for j in range(2,x+1):
        if(x!=j and x % j == 0):
            f = 1
            break

    if(f==0):
        lis.append(x)
print("Prime Numbers Between 1 to 100:")
print(*lis,end=' ')
print()

f = open('testt2.txt','r')
for a in f:
    num = int(a)
    if (num % 2 == 0): 
        even = open("even.txt","a") 
        even.write(str(num)) 
        even.write("\n") 
    else: 
        odd = open("odd.txt","a") 
        odd.write(str(num)) 
        odd.write("\n")
z = open("words.txt","rt")
print(z.read())
    

fa = open('test.txt','a')
for x in range(1,6):
    data = input("Enter Your Data: ") 
    fa.write(data)
fa.close()
fa = open('test.txt','r')
print(fa.read())

import difflib
  
with open('file1.txt') as file_1:
    file_1_text = file_1.readlines()
  
with open('file2.txt') as file_2:
    file_2_text = file_2.readlines()
  
# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='file1.txt', 
        tofile='file2.txt', lineterm=''):
    print(line)


errors = []                       # The list where we will store results.
linenum = 0
substr = "specific".lower()          # Substring to search for.
with open ('Homework21.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
for err in errors:
    print(err)

b = open("newfile1.txt","w")
b = open("newfile1.txt","a")
b.write("This is one line\n")
b.write("This is one line\n")
b.write("This is one line\n")
b.write("This is one line\n")
b.write("This is one line\n")
b=open("newfile1.txt","rt")
print(b.read())
b.close()
l = open("newfile2.txt","w")
l = open("newfile2.txt","a")
l.write("Age: 10, Name: Shaheer, City: Sharjah")
l = open("newfile2.txt","rt")
print(l.read())

a = open("para.txt","rt")
print(a.read())
