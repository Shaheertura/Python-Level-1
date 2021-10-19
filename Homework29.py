
class employees:
    e1 = {
        "Name":"Mohammad",
        "Gender":"Male",
        "Age":"31"
        }
    e2 = {
        "Name":"Evan",
        "Gender":"Male",
        "Age":"29"
        }
    e3 = {
        "Name":"Ahmad",
        "Gender":"Male",
        "Age":"32"
        }
    e4 = {
        "Name":"Elias",
        "Gender":"Male",
        "Age":"35"
        }
    e5 = {
        "Name":"Sarah",
        "Gender":"Female",
        "Age":"31"
        }
e = employees()
'''
print(e.e1)
print(e.e2)
print(e.e3)
print(e.e4)
print(e.e5)
'''

class animal:
    aname = "Fox"
    acolor = "Orange"
    aeyes = "Blue"
a = animal()
print("Name:",a.aname,"   Color:",a.acolor,"   Eye Color:",a.aeyes)

class fruits:
    fname = "Orange"
    fcolor = "Orange"
    fshape = "Circle"
f = fruits()
print()
print("Name:",f.fname,"   Color:",f.fcolor,"   Circle:",f.fshape)

class vegs:
    vname = "Cauli Flower"
    vcolor = "Green and White"
    vshape = "Circle"
v = vegs()
print()
print("Name:",v.vname,"   Color:",v.vcolor,"   Circle:",v.vshape)

class stu:
    s1name = "Hamzah"
    s1age = "9"
    s1gender = "Male"
    
    s2name = "Mohammad"
    s2age = "10"
    s2gender = "Male"
    
    s3name = "Ali"
    s3age = "11"
    s3gender = "Male"

    s4name = "Zahra"
    s4age = "10"
    s4gender = "Female"
s1 = (stu.s1name,stu.s1age,stu.s1gender)
print(s1)
print()
s2 = (stu.s2name,stu.s2age,stu.s2gender)
print(s2)
print()
s3 = (stu.s3name,stu.s3age,stu.s3gender)
print(s3)
print()
s4 = (stu.s4name,stu.s4age,stu.s4gender)
print(s4)
print()
class depart:
    dname = "The Hosptial of Hawkins"
    ddep = "Hospital"
    dempl = "3042"
    dloc = "USA UTAH 22 Route"
d = depart()

print("Name:",d.dname,"   Department:",d.ddep,"   Employees:",d.dempl,"   Location:",d.dloc)
print()
class school:
    sname = "Towheed Iranian School"
    ssubjects = "Arabic Farsi English \nMath PE Social Studies Quran"
    sgrades = "Grade 1 - 12"
    sloc = "UAE Dubai Sheikh Zayed Road"
s = school()
print("Name:",s.sname,"   Subjects:",s.ssubjects,"   Grades:",s.sgrades,"   Location:",s.sloc)
print()
class country:
    cname = "Canada"
    cpop = "38,103,773"
    cloc = "Nort America"
    cseasons = "Winter Fall Spring Summer"
c = country()
print("Name:",c.cname,"   Population:",c.cpop,"   Location:",c.cloc,"   Seasons:",c.cseasons)
print()
class city:
    ccname = "Montreal"
    ccpro = "Quebec"
    ccpop = "4,221,000"
    ccloc = "North America"
    cccoun = "City in Canada"
cc = city()
print("Name:",cc.ccname,"   Province: ",cc.ccpro,"   Population:",cc.ccpop,"   Location:",cc.ccloc,"   Country:",cc.cccoun)
print()
class car:
    caname = "Tesla"
    catype = "Electric"
    camodel = "Model X Model 3 Model S Model Y Cybertruck"
    cafe = "Autoatic Driving Games in the ipad full access from car with Phone Card is the key"
ca = car()

print("Name:",ca.caname,"   Type:",ca.catype,"   Models:",ca.camodel,"   New Features:",ca.cafe)
print()
class sta:
    stname = "Ruler"
    stlen = "30cm"
    stus = "Calculatuing the length of objects"
sta = sta()
print("Name:",sta.stname,"   Length:",sta.stlen,"   Use:",sta.stus)

