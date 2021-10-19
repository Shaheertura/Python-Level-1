
banner = ("""
 ______     __  __     ______     __  __     ______     ______     ______    
/\  ___\   /\ \_\ \   /\  __ \   /\ \_\ \   /\  ___\   /\  ___\   /\  == \   
\ \___  \  \ \  __ \  \ \  __ \  \ \  __ \  \ \  __\   \ \  __\   \ \  __<   
 \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_/\/_/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/ 
                                                                             

""")
print(banner)







listt = []
atuple = (50,60)
listt.append(atuple)
atuple = (50,60)
print("Before",atuple)
atuple=list(atuple)
atuple.append(80)
print("After",atuple)

list2 = []
btuple = (80)
ctuple = (100)
dtuple = (30)
list2.append(btuple)
list2.append(ctuple)
list2.append(dtuple)
print(list2)
num = int(input("Enter a number: "))
if num in list2:
    print("Correct")
else:
    print("Not Correct")
list3 = []
credit1 = (4582950256)
credit2 = (9275628594)
list3.append(credit1)
list3.append(credit2)
print(list3)
credit = int(input("Enter a credit card number: "))
print("Validating ...")
if credit in list3:
    print("Correct")
else:
    print("Not Valid Credit Card")

tuplee = (5,6,8,2)
print(tuplee)
tuplee1 = tuplee[0]
tuplee2 = tuplee[1]
tuplee3 = tuplee[2]
tuplee4 = tuplee[3]
print("Multiplied",tuplee1*tuplee2*tuplee3*tuplee4)

aTuple = (10, 20, 30, 40)
print(aTuple)
tuplex = aTuple[0]
tuplex2 = aTuple[1]
tuplex3 = aTuple[2]
tuplex4 = aTuple[3]
print(tuplex)
print(tuplex2)
print(tuplex3)
print(tuplex4)

loltuple = (60,40,70,80)
loltuple1 = (10,50,30,70)
print(loltuple)
print(loltuple1)
loltuple=list(loltuple)
loltuple1=list(loltuple1)
xcv = loltuple
loltuple = loltuple1
loltuple1 = xcv
print("Switched",loltuple,loltuple1)
