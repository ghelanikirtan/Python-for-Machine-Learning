# Importing random module for random integer number
import random

# importing os module for holding screen
import os       # os.system('pause')


cpu_win = 0
user_win = 0


options_rps = ['rock', 'paper', 'scissors']

print("Welcome! to Rock-Paper-Scissors Game")
userName = input("Enter username : \n> ")
if userName != '':
    print("Let's start the game :D")

print("Type Rock/Paper/Scissors or 'Q' to Quit : ")

i=0
while True:
    userChoice = input("> ").lower()
    if userChoice == 'q':    
        break
    i+=1

    if userChoice not in options_rps:
        print("\tType valid answer!, {}".format(userName))
        continue

    # using randint function from random module to get random no.s in given range
    randomNumber = random.randint(0,2)
    cpuChoice = options_rps[randomNumber].lower()

    print("Computer picked : ",cpuChoice)

    if userChoice == 'rock' and cpuChoice == 'scissors':
        user_win += 1
        print("\tWhoa!!! you WON..., ",userName)
        continue
    elif cpuChoice == 'rock' and userChoice == 'scissors':
        cpu_win += 1
        print("\tOOPS!!! wrong pick...")
        continue

    if userChoice == 'paper' and cpuChoice == 'rock':
        user_win += 1
        print("\tWhoa!! you win this round, ",userName)
        continue
    elif cpuChoice == 'paper' and userChoice == 'rock':
        cpu_win += 1
        print("\tOOPS!! wrong pick....")
        continue


    if userChoice == 'scissors' and cpuChoice == 'paper':
        user_win += 1
        print("\tWhoa!! you win this round, ",userName)
        continue
    elif cpuChoice == 'scissors' and userChoice == 'paper':
        cpu_win += 1
        print("\tOOPS!! wrong pick....")
        continue

    if userChoice == cpuChoice:
        print('''\t( >-< )
Tied... ''')
        continue
   

    


if i!=0:   
    print("--------------------------------------------") 
    print("{}'s Score : {}".format(userName, user_win))
    print("CPU's Score : {}".format(cpu_win))
    if user_win > cpu_win: 
        print("\tCONGRATULATIONS!\nYou win the game!!!")
    elif user_win < cpu_win:
        print("\tT-T\nYou loose the game !!!")
    else : print("Match Tied : )")
    
print("\nGoodbye! Have a nice day...\n")

os.system('pause')

    

