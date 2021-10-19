try:
    from random import randint
    import sys
except:
    print("[!]Your Python Coudnt Import these Modules\nPython Either needs TO be REINSALLED OR REPAIRED[!]")
def banner():
    banner1 = """
 _                     _            
| |                   | |           
| |     ___   ___ __ _| |_ ___ _ __ 
| |    / _ \ / __/ _` | __/ _ \ '__|
| |___| (_) | (_| (_| | ||  __/ |   
\_____/\___/ \___\__,_|\__\___|_|   
                                    
                         
                                 """
    banner2= """
██╗      ██████╗  ██████╗ █████╗ ████████╗███████╗██████╗ 
██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██║     ███████║   ██║   █████╗  ██████╔╝
██║     ██║   ██║██║     ██╔══██║   ██║   ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                          
                                                                    
                                                                                                                                                                        
                                                  """
    banner3 = """
 #                                                
 #        ####   ####    ##   ##### ###### #####  
 #       #    # #    #  #  #    #   #      #    # 
 #       #    # #      #    #   #   #####  #    # 
 #       #    # #      ######   #   #      #####  
 #       #    # #    # #    #   #   #      #   #  
 #######  ####   ####  #    #   #   ###### #    # 
                                                  
                                                       
                                                                                                                                   
"""
    banners = [banner1,banner2,banner3]
    print(banners[randint(0,2)])
banner()
names = ("""
Island Grill
Flavoroso
Green Curry
El Pirata Porch
Sweet Escape
Salty Squid

""")
firstres = {"Name":"Island Grill",
            "rating":"4",
            "no":"212-200-3112",
            "Location":"21 First Avenue",
            "email":"islandgrill@buissness.com",
            "travel":"Car",
            "timings":"Daily 10:00 AM to 11:00 PM"
            }

secondres = {"Name":"Flavoroso",
             "rating":"5",
             "no":"212-534-5632",
             "Location":"21 Route",
             "email":"flavoroso@buissness.com",
             "travel":"Car",
             "timings":"Daily 10:00 AM to 11:00 PM"
             }

thirdres = {"Name":"Green Curry",
            "rating":"4.5",
            "no":"212-393-2957",
            "Location":"21 First Road",
            "email":"greencury@buissness.com",
            "travel":"Car",
            "timings":"Daily 10:00 AM to 11:00 PM"
            }

fourthres = {"Name":"El Pirata Porch",
             "rating":"3.5",
             "no":"212-202-0742",
             "Location":"54 Main Street",
             "email":"elpiratapoarch@buissness.com",
             "travel":"Car",
             "timings":"Daily 10:00 AM to 11:00 PM"
    }
fifthres = {"Name":"Sweet Escape",
            "rating":"5",
            "no":"212-204-1455",
            "Location":"32 Avenue",
            "email":"sweetescape@buissness.com",
            "travel":"Car",
            "timings":"Daily 10:00 AM to 11:00 PM"

    }
sixres = {"Name":"Salty Squid",
          "rating":"5",
          "no":"212-205-7162",
          "Location":"12 Street",
          "email":"saltysquid@buissness.com",
          "travel":"Car",
          "timings":"Daily 10:00 AM to 11:00 PM"

    }
print("Locations Near me:")
print("1-",firstres.get("Name"))
print("2-",secondres.get("Name"))
print("3-",thirdres.get("Name"))
print("4-",fourthres.get("Name"))
print("5-",fifthres.get("Name"))
print("6-",sixres.get("Name"))

op = int(input("Which Resturant do you Want?: "))
if op == 1:
    print()
    print("Info",firstres)
    print()
    print("Location:",firstres.get("Location"))
elif op == 2:
    print()
    print("Info",secondres)
    print()
    print("Location:",secondres.get("Location"))
elif op == 3:
    print()
    print("Info",thirdres)
    print()
    print("Location:",thirdres.get("Location"))
elif op == 4:
    print()
    print("Info",fourthres)
    print()
    print("Location:",fourtres.get("Location"))
elif op == 5:
    print()
    print("Info",fifthres)
    print()
    print("Location:",fifthres.get("Location"))
elif op == 6:
    print()
    print("Info",sixtres)
    print()
    print("Location:",sixres.get("Location"))
else:
    print("Invalid Option")
    sys.exit()
