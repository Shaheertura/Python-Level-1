try:
    from random import randint
    import sys
except:
    print("[!]Your Python Coudnt Import these Modules\nPython Either needs TO be REINSALLED OR REPAIRED[!]")
def banner():
    banner1 = """
 _____       _     
|  _  |     (_)    
| | | |_   _ _ ____
| | | | | | | |_  /
\ \/' / |_| | |/ / 
 \_/\_\\__,_|_/___|
                   
                   
                                    
"""
    banner2= """
 ██████╗ ██╗   ██╗██╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝
██║   ██║██║   ██║██║  ███╔╝ 
██║▄▄ ██║██║   ██║██║ ███╔╝  
╚██████╔╝╚██████╔╝██║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
                             
                                                                    
                                                                                                                                                                        
                                                  """
    banner3 = """
  #####                  
 #     # #    # # ###### 
 #     # #    # #     #  
 #     # #    # #    #   
 #   # # #    # #   #    
 #    #  #    # #  #     
  #### #  ####  # ###### 
                                                  
                                                       
                                                                                                                                   
"""
    banners = [banner1,banner2,banner3]
    print(banners[randint(0,2)])
banner()
#----------------Main-----------------------#
wrong = 0
t = True
print("1-Sports\n2-Maths\n3-Science\n4-English")
subject = int(input("Enter a Subject: "))

if subject == 1:
    while t == True:
        question1 = input("Who Made a World Record for the Longest Field Goal: ")
        question1 = question1.title()
        answer1 = "Matt Prater"
        if question1 == answer1:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True

    while t == True:
        question2 = input('What sport is described as “the beautiful game?”: ')
        question2 = question2.title()
        answer2 = "Association Football"
        if question2 == answer2:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True
        
    while t == True:
        
        question3 = input("Which country won the first ever football world cup: ")
        question3 = question3.title()
        answer3 = "Uruguay"
        if question3 == answer3:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True


    while t == True:
        question4 = input("How many regulation strokes are there in swimming: ")
        question4 = question4.title()
        answer4 = "Four"
        if question4 == answer4:
            print("Correct Answer")
            t = False
        elif question4 == "4":
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True
        
    while t == True:
        question5 = input("How long is the total distance of a marathon: ")
        question5 = question5.title()
        answer5 = "Twenty Six"
        if question5 == answer5:
            print("Correct Answer")
            print("The Quiz is Finished!")
            t = False
        elif question5 == "26":
            print("Correct Answer")
            print("The Quiz is Finished!")
            print("You got",wrong,"Wrongs")
            t = False
            
        else:
            print("Wrong")
            wrong = wrong + 1

    if t == False:
        t = True
        
elif subject == 2:
    while t == True:
        question1 = input("What is 12 X 12: ")
        answer1 = "144"
        if question1 == answer1:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True

    while t == True:
        question2 = input("What does Parenthiseis Exponent Multiplication Division Addition and Subtracion Stand for: ")
        question2 = question2.upper()
        answer2 = "PEMDAS"
        if question2 == answer2:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1

    if t == False:
        t = True
        
    while t == True:
        
        question3 = input("Write the Equivelant Fraction of 1/2: ")
        answer3 = "2/4"
        if question3 == answer3:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True


    while t == True:
        question4 = input("7 X 12 / 2: ")
        answer4 = "42"
        if question4 == answer4:
            print("Correct Answer")
            t = False
        elif question4 == "4":
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True
        
    while t == True:
        question5 = input("20 / 5 * 6 - 3: ")
        question5 = question5.title()
        answer5 = "Twenty One"
        if question5 == answer5:
            print("Correct Answer")
            print("The Quiz is Finished!")
            t = False
        elif question5 == "21":
            print("Correct Answer")
            print("The Quiz is Finished!")
            print("You got",wrong,"Wrongs")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
            
elif subject == 3:
    if t == False:
        t = True
    while t == True:
        t = False
        print("What is the universe made of")
        print()
        print("""
        Multiple Choice Question

1-Normal Matter
2-Dark Matter
3-Dark Energy
4-All Above
""")
    t = True
    question1 = input("Enter the Number: ")
    if question1 == "4":
        print("Correct Answer")
        t = False
    else:
        print("Wrong")
        wrong = wrong + 1
    if t == False:
        t = True

    while t == True:
        question2 = input('This essential gas is important so that we can breath: ')
        question2 = question2.title()
        answer2 = "Oxygen"
        if question2 == answer2:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True
        
    while t == True:
        
        question3 = input("What is the nearest planet to the sun: ")
        question3 = question3.title()
        answer3 = "Mercury"
        if question3 == answer3:
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True


    while t == True:
        question4 = input("How many teeth does an adult human have: ")
        question4 = question4.title()
        answer4 = "Thirty Two"
        if question4 == answer4:
            print("Correct Answer")
            t = False
        elif question4 == "32":
            print("Correct Answer")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True
        
    while t == True:
        question5 = input("What do bees collect and use to create honey: ")
        question5 = question5.title()
        answer5 = "Nectar"
        if question5 == answer5:
            print("Correct Answer")
            print("The Quiz is Finished!")
            print("You got",wrong,"Wrongs")
            t = False
        else:
            print("Wrong")
            wrong = wrong + 1
    if t == False:
        t = True
elif subject == 4:
    t = True
    question1 = input("what is the plural form of sheep: ")
    questoon1 = question1.title
    if question1 == "Sheep":
        print("Correct Answer")
        t = False
    else:
        print("Wrong")
        wrong = wrong + 1
        
    if t == False:
        t = True
    while t == True:
        t = False
        print(" I spoke to ____")
        print()
        print("""
        Multiple Choice Question

1-She
2-Her
""")
    t = True
    question2 = input("Enter the Number: ")
    if question2 == "2":
        print("Correct Answer")
        t = False
    else:
        print("Wrong")
        wrong = wrong + 1
    if t == False:
        t = True

    while t == True:
        t = False
        print("Where ____ you come from?")
        print()
        print("""
        Multiple Choice Question

1-Do
2-Are
""")
    t = True
    question3 = input("Enter the Number: ")
    if question3 == "1":
        print("Correct Answer")
        print("The Quiz is Finished")
        print("You got",wrong,"Wrongs")
        t = False
    else:
        print("Wrong")
        wrong = wrong + 1
        

        
                        
























