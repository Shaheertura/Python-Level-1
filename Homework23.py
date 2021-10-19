try:
    from random import randint
    import sys
except:
    print("[!]Your Python Coudnt Import these Modules\nPython Either needs TO be REINSALLED OR REPAIRED[!]")
def banner():
    banner1 = """
  ___      _           _         _             
 / _ \    | |         (_)       (_)            
/ /_\ \ __| |_ __ ___  _ ___ ___ _  ___  _ __  
|  _  |/ _` | '_ ` _ \| / __/ __| |/ _ \| '_ \ 
| | | | (_| | | | | | | \__ \__ \ | (_) | | | |
\_| |_/\__,_|_| |_| |_|_|___/___/_|\___/|_| |_|
                                               
                                                                       
                                 
                                 """
    banner2= """
 █████╗ ██████╗ ███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
███████║██║  ██║██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║
██╔══██║██║  ██║██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║
██║  ██║██████╔╝██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                    
                                                                                                                                                                        
                                                  """
    banner3 = """
    #                                                  
   # #   #####  #    # #  ####   ####  #  ####  #    # 
  #   #  #    # ##  ## # #      #      # #    # ##   # 
 #     # #    # # ## # #  ####   ####  # #    # # #  # 
 ####### #    # #    # #      #      # # #    # #  # # 
 #     # #    # #    # # #    # #    # # #    # #   ## 
 #     # #####  #    # #  ####   ####  #  ####  #    # 
                                                       
                                                                                                                                   
"""
    banners = [banner1,banner2,banner3]
    print(banners[randint(0,2)])
banner()
#----Main------#

def func():
    whitelist = []
    terms = ("""
                    Terms of Service
    Please Read the Terms and Service We will need Your name Date 
    of Birth and Adress We Wont share Any info with any third party Companies
    We hope you have a Wonderfuk day at the Academy
    """)
    print(terms)

    print("""
    Keep in Mind This Info Is NOT SHARED
    """)
    name = input("Enter your Name Please: ")
    dob = input("Enter Your Date of Birth Please: ")
    adress = input("Enter Your Adress Please: ")
    print("Please wait")
    whitelist.append(name)
    whitelist.append(dob)
    whitelist.append(adress)
    print("These are the Details you entered",*whitelist,"if these are Correct Enter y if wrong enter n")
    noy=input("Enter here: ")
    if noy=="y":
        print("Congrats You finished Youre Officialy inside the Course")
    else:
        print("Terminating")
        sys.exit()
print("Which Subject would you like?\n1-Arts and Science\n2-Commerce Stream")
print("""
    #------------------------#
    Congrats On passing 10th Grade
    #------------------------#
""")
op = int(input("Enter the Number: "))
    
if op == 1:
  func()
elif op == 2:
    func()
else:
    print("Invalid")
    sys.exit()
            
        

        
        

















