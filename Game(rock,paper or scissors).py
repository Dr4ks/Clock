#You are welcome for playing a famous game called rock,paper or scissors

import random
while True:

    choices=["rock","paper","scissors"]
    computer=random.choice(choices)

    player=None

    while player not in choices:
        player=input("Choose one of them(ex.rock,paper or scissors)=>=>").lower()

    if player==computer:
        print("Player=>%s"%player)
        print("Computer=>%s"%computer)
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
            print("Player=>%s"%player)
            print("Computer=>%s"%computer)
            print("You lost!")
        if computer=="scissors":
            print("Player=>%s"%player)
            print("Computer=>%s"%computer)
            print("You won!")
    elif player=="paper":
        if computer=="rock":
            print("Player=>%s"%player)
            print("Computer=>%s"%computer)
            print("You won!")
        if computer=="scissors":
            print("Player=>%s"%player)
            print("Computer=>%s"%computer)
            print("You lost!")
    elif player=="scissors":
        if computer=="rock":
            print("Player=>%s"%player)
            print("Computer=>%s"%computer)
            print("You lost!")
        if computer=="paper":
            print("Player=>%s"%player)
            print("Computer=>%s"%computer)
            print("You won!")
    play_again=input("Play again? (yes/no)=>").lower()

    if play_again!="yes":
        break
print("Have a good day")



        

            



        


    
