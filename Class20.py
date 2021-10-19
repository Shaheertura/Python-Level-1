#-------Lib and Modules-----------------#
try:
    from random import randint              
    import time                             
except:
    print("[!]Python cannot import Modules \nPython need to Be Reinstalled or Repaired")                          
                                        
#-------------------Design--------------#
def banner():
    banner1 = """
______             _             
| ___ \           | |            
| |_/ / ___   ___ | | _____ _ __ 
| ___ \/ _ \ / _ \| |/ / _ \ '__|
| |_/ / (_) | (_) |   <  __/ |   
\____/ \___/ \___/|_|\_\___|_|   
                                 
                                 """
    banner2= """
██████╗  ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██╔══██╗██║   ██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                  """
    banner3 = """
 ######                                     
 #     #  ####   ####  #    # ###### #####  
 #     # #    # #    # #   #  #      #    # 
 ######  #    # #    # ####   #####  #    # 
 #     # #    # #    # #  #   #      #####  
 #     # #    # #    # #   #  #      #   #  
 ######   ####   ####  #    # ###### #    # 
                                            """
    banner4 = """
________            ______              
___  __ )______________  /______________
__  __  |  __ \  __ \_  //_/  _ \_  ___/
_  /_/ // /_/ / /_/ /  ,<  /  __/  /    
/_____/ \____/\____//_/|_| \___//_/     
                                        """
    banners = [banner1,banner2,banner3,banner4]
    print(banners[randint(0,3)])
banner()
#-----------------Info-----------------#
info = ['Canada','U.A.E','Inida','USA','Kazhikstan','Afghanistan','Iran','Turkey','Phillepense','Uganda','Africa','Indonesia','France']
print()
print(info)
source = input("Write from which Country you want to travel: ")
#verifier
print("Validating Country")
time.sleep(3)
if source in info:
    print("Valid Country :)")
    print()
    dest = input("Enter the Country you want to enter: ")
    print("Validating Country")
    time.sleep(3)
else:
    print("Not Valid Country")
    exit()
if dest in source:
    print("Cant go to the same Country you are in")
    exit()
if dest in info:
        print("Valid Country")
        print()
else:
        print("Not Valid Country :(")
        exit()

travels = ("Valid Travels: Rail, Bus, Airplane")
print(travels)
travel = input("How do you want to travel: ")
otravel = ("Airplane","Rail")
ootravel = ("Bus")
if travel in otravel:
    print("Great Please Wait...")
    time.sleep(1)
    classes = ["1st Class","2nd Class","3rd Class"]
    print(classes)
    clas = input("Enter which Class You want: ")
    class1 = "1st Class"
    class2 = "2nd Class"
    class3 = "3rd Class"
Prices = {'Canada':25000,'U.A.E':20000,'India':17000,'USA':30000,'Kazhikstan':3000,'Afghanistan':1000,'Iran':5000,'Turkey':25000,'Phillepense':7000,'Uganda':5000,
          'Africa':10000,'Indonesia':9000,'France':30000}
if travel in ootravel:
    if dest in Prices.keys():
        bus = Prices.get(dest)
        taxes = bus*5/100
        grandtotal = bus + taxes
        print("The GrandToal is",grandtotal,"Plus Taxes")



Prices = {'Canada':25000,'U.A.E':20000,'India':17000,'USA':30000,'Kazhikstan':3000,'Afghanistan':1000,'Iran':5000,'Turkey':25000,
          'Phillepense':7000,'Uganda':5000,
          'Africa':10000,'Indonesia':9000,'France':30000}
try:
    if clas in classes:
        print("Set")
    
    if dest in Prices.keys():
        a = Prices.get(dest)
    taxes = a*5/100
    if class1 in clas:
        b = 2500
        total = a + b + taxes
        print("The Grand Total is",total,"Plus Taxes")
    elif class2 in clas:
        c = 1500
        total = a + c + taxes
        print("The Grand Total is",total,"Plus Taxes")
    elif class3 in clas:
        d = 500
        total = a + d + taxes
        print("The Grand Total is",total,"Plus Taxes")

    



                

   




except:
    pass
