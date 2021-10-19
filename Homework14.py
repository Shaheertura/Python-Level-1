blank= []
usrblank = input("Enter anything to add in the list: ")
blank.append(usrblank)
print(blank)

eg = [1,3,5,7,9]
print("Before:",eg)
eg.clear()
eg = [2,4,6,8,10]
print("After:",eg)
print()
eg2 = ["a","b","c","d"]
print("Before:",eg2)
eg2a = eg2[0]
eg2b = eg2[-1]
eg2.pop(0)
eg2.pop(-1)
eg2.append(eg2a)
eg2.insert(0,eg2b)
print("After:",eg2)
print()

eg3 = [1,-2,3,4,-5,6,-7,-8,9]
if eg3 < 0:
    print(eg3)
elif eg3 > 0:
    print("")

'''
eg4 = [1,2,3,4,5,6,7,8,9]
if eg4 % 2 ==0:
    print(eg4, "Even")
elif eg4 % 2 != 0:
    print(eg4, "Odd")
else:
    print("")
'''

