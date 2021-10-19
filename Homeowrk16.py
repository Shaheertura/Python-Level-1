import time
import pandas as pd
a = [2,5,6,9,4]
b = [2,4,6,8,2]
acopy = [2,5,6,9,4]
bcopy = [2,4,6,8,2]
i = 0
j = 0
i2 = 0
j2 = 0
st = 5
stt = 0
intersection = []
complement = []
print("Before",a,"\nBefore",b)
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        intersection.append(a[i])
        i += 1
        j += 1
    elif a[i] > b[j]:
        j += 1
    else:
        i += 1
while i2 < len(acopy) and j2 < len(bcopy):
    if acopy[i2] != bcopy[j2]:
        complement.append(acopy[i2])
        i2 += 1
        j2 += 1
    elif acopy[i2] > bcopy[j2]:
        j2 += 1
    else:
        i2 += 1

print(intersection)
print(complement)

scores = {'Tom':'Math', 'Mohammad':'Science', 'Shaheer':'English','Sarah':'Art', 'Kyle':'P.E'}
print(scores)
work1 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work2 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work3 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work4 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work5 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work6 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work7 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work8 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work9 = input("Enter your record: ")
print("Next Employe Please ...")
time.sleep(1)
work10 = input("Enter your record: ")
print("Adding Items to List ...")
time.sleep(5)
records = {'1': work1, '2': work2,'3':work3, '4': work4, '5':work5, '6': work6, '7': work7, '8': work8, '9':work9, '10':work10}
recordslist = []
recordslist.append(records)
df = pd.DataFrame(recordslist)
print(df.head())
'''
owlist = []
ow = {3,5,6,2}
ow2 = {2,2,6,2}
owlist.append(ow)
owlist.append(ow2)
print(owlist)

listlist = []
list1 = [11, -21, 0, 45, 66, -93]
print("Before",list1)
# iterating each number in list
for num in list1:
    # checking condition
    if num >= 0:
       listlist.append(num)
print(listlist)

tuplee = (1,2,3,5,6,3,5)
print(type(tuplee))

print("Before",tuplee)
tuplee = list(tuplee)
tuplee.append("New")
print("After",tuplee)
tuplee = tuple(tuplee)
print(type(tuplee))
'''
eo = [1,2,3,4,5,6,7,8,9]
for evenodd in eo:
    if evenodd % 2 != 0:
        evenodd.pop()
'''
creditcard = ['4251722562 ''4244285374 ''8765907679 ''8976467679']
print(creditcard)
num1 = int(input("Enter Credit card Number: "))
num2 = int(input("Enter Credit card Number: "))
num3 = int(input("Enter Credit card Number: "))
num4 = int(input("Enter Credit card Number: "))
if num1 in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Valid")
elif num2 in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Valid")
elif num3 in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Valid")
elif num4 in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Valid")
elif num1 not in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Not Valid")
elif num1 not in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Not Valid")
elif num2 not in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Not Valid")
elif num3 not in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Not Valid")
elif num4 not in creditcard:
    print("Validating...")
    time.sleep(2)
    print("Not Valid")

print("\rAdding Items to list...")
time.sleep(10)

creditnumbers = {'num1':num1,'num2':num2,'num3':num3,'num4':num4}
print(creditnumbers)
'''
