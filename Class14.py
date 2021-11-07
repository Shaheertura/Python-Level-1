'''
a=(1,3.5,1,True,"CodeYoung")
print(len(a))
print(a[0])
print(a[-1])
print(a[1:4])
print(a[:4])
print(a[2:])
print(a[-4:-1])
b=(a,4,"Hello",False)
print(b)
print(type(b))

a=("apple","mango","pear")
b=list(a)
b[1] = "kiwi"
b.append("strawberry")
b.remove("apple")
a=tuple(b)
print(a)
del a

a = ("apple","mango","pear")
(red,yellow,green)=a
print(red)
print(yellow)
print(green)

a=("apple","mango","apple","pear")
b=a.count("apple")
print(b)
c=a.index("mango")
print(c)
a=("apple","mango","apple","pear")
b=(12,3,4)
c=a+b
print(c)
m=a*2
print(m)

a= ("apple","mango","apple","pear")

for i in range(len(a)):
    print(a[i])
'''
a=("apple","mango","apple","pear")
i=0
while i<len(a):
    print(a[i])
    i+=1



















    















