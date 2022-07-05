import random

def play():
    user = input("Choose your hand. You can choose 'rock', 'paper' or 'scissors' ").lower()
    comp = random.choice(['rock', 'paper', 'scissors'])

    if user == "rock":
        if comp == "rock":
            print("It's a draw with both players picking rock")
        elif comp == "paper":
            print("The computer beat your rock with paper. You lose")
        else:
            print("You beat the computer's scissors with rock. Congratulations, you win")
    elif user == "paper":
        if comp == "rock":
            print("You beat the computer's rock with paper. Congratulations, you win")
        elif comp == "paper":
            print("It's a draw with both players picking paper")
        else:
            print("The computer beat your paper with scissors. You lose")
    else:
        if comp == "rock":
            print("The computer beat your scissors with rock. You lose")
        elif comp == "paper":
            print("You beat the computer's paper with scissors. Congratulations, you win")
        else:
            print("It's a draw with both players picking scissors")

    
play()