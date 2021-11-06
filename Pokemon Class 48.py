
'''

power = [3,8,9,7]
minimum, maximum = 0,0
for p in power:
    if minimum == 0 and maximum == 0:
        minimun,maximum = power[0],power[0]
        print(minimum,maximum)
    else:
        minimum = min(minimum,p)
        maximum = max(maximum,p)
        print(maximum)


powers = [3, 8, 9, 7]

mini, maxi = 0, 0

for power in powers: 

    if mini == 0 and maxi == 0: 

        mini, maxi = powers[0], powers[0] 

        print(mini, maxi) 

    else: 

        mini = min(mini, power) 

        maxi = max(maxi, power) 

        print(mini, maxi)



'''




pikachu = {
    'Name':'Pikachu','Health':60,'type':'Electric','maxp':120,'minp':50
    }
joleton = {
    'Name':'Joleton','Health':160,'type':'Electric','maxp':100,'minp':30
    }
thundurus = {
    'Name':'Thundurus','Health':110,'type':'Electric','maxp':80,'minp':0
    }
zekrom = {
    'Name':'Zekrom','Health':130,'type':'Electric','maxp':120,'minp':0
    }

luxio = {
    'Name':'luxio','Health':80,'type':'Electric','maxp':10,'minp':0
    }

pik= [pikachu.get('maxp'),pikachu.get('minp')]
jol = [joleton.get('maxp'),joleton.get('minp')]
thun = [thundurus.get('maxp'),thundurus.get('minp')]
zek = [zekrom.get('maxp'),zekrom.get('minp')]
lex = [luxio.get('maxp'),zekrom.get('minp')]

power = [pik[0],pik[1],jol[0],jol[1],thun[0],thun[1]
          ,zek[0],zek[1],lex[0],lex[1]]
print("1-Pikachu\n2-Jolten\n3-Thunderus\n4-Zekrom\n5-Luxio")
pokask = int(input("Enter the Pokemon You want to find Your Values for: "))

if pokask == 1:

    print("Minimum Power:",min(pik))
    print("Maximum Power:",max(pik))
    
elif pokask == 2:
    
    print("Minimum Power:",min(jol))
    print("Maximum Power:",max(jol))
elif pokask == 3:
    print("Minimum Power:",min(thun))
    print("Maximum Power:",max(thun))
    
elif pokask == 4:
    

    print("Minimum Power:",min(zek))
    print("Maximum Power:",max(zek))
elif pokask == 5:

    print("Minimum Power:",min(lex))
    print("Maximum Power:",max(lex))
else:
    print("Invalid Choice")

    
    







