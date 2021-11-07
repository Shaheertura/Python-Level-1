"""SET-----
{}
a={"apple",1,6,5,True}
b={"apple","cherry","mango"}
t={"pineapple","papaya"}
print(a)
print(len(a))
print(type(a))

for i in a:
    print(i)
print("apple" in a)
b.add("orange")
print(b)
b.update(a)
print(b)
b.update(t)
print(b)
del b
print(b)
a={"apple","cherry","mango"}
b={1,2,3}
c=a.union(b)
print(c)
a.update(b)
print(c)
#a.update(b)
#print(a)
e=a.intersection(b)
print(e)

Dictionary------------


a={1:"a",2:"b",3:"c",4:"d"}
print(a)
print(len(a))
print(type(a))
print(a.values())
print(a.keys())
print(a.items())"""

a={1,2,3,4,5,6}
b={"apple","mango","orange","guava",1,3}
print(a | b)
print(a & b)
print(a - b)

