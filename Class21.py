#-----Lib and Modules-------#
try:
    import random
    import sys
except:
    print("[!]Python cannot import Modules \nPython need to Be Reinstalled or Repaired")

#---------------------------#
#------Design---------------
def banner():
    print("""
    #---------------------#
      Rock Paper Scissors     Made By Shaheer :)
           Shoot!
    #---------------------#
    """)
banner()
#---------------------------#
def main():
#------------Player1------------------#
    items = ["Rock","Paper","Scissors"]
    print("Valid Charecters:",items)
    player1 = input("Enter a Charecter: ")
    #verify
    if player1 in items:
        print("Great")
    else:
        print("Not Valid")
        exit()
    #-------------------------------------#
    #---------------Player2---------------#
    player2 = input("Enter a Charecter: ")
    if player2 in items:
        print("Great")
    else:
        print("Not Valid")
        exit()
    #-------------------------------------#
    #--------Main---------#
    if player1 == "Rock" and player2 == "Scissors":
        print(player1,"Wins!")
    elif player1 == "Rock" and player2 == "Paper":
        print(player1,"Wins!")
    elif player1 == "Paper" and player2 == "Rock":
        print(player1,"Wins")
    elif player1 == "Paper" and player2 == "Scissors":
        print(player1,"Wins")
    elif player1 == "Scissors" and player2 == "Rock":
        print(player1,"Wins")
    elif player1 == "Scissors" and player2 == "Paper":
        print(player1,"Wins")
    elif player1 == player2:
        print("Tie!")
    elif player2 == "Rock" and player1 == "Scissors":
        print(player2,"Wins!")
    elif player2 == "Rock" and player1 == "Paper":
        print(player2,"Wins!")
    elif player2 == "Paper" and player1 == "Rock":
        print(player2,"Wins")
    elif player2 == "Paper" and player1 == "Scissors":
        print(player2,"Wins")
    elif player2 == "Scissors" and player1 == "Rock":
        print(player2,"Wins")
    elif player2 == "Scissors" and player1 == "Paper":
        print(player2,"Wins")
    elif player2 == player1:
        print("Tie!")

#---------------------#
if __name__ == '__main__':
    main()












