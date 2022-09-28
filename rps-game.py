import random

def rps():
    turns = ["rock", "paper", "scissors"]

    human_turn = input("Input human turn: ")

    computer_turn = random.choice(turns)

    print(f"Human: {human_turn} vs Computer: {computer_turn}")

    if human_turn == computer_turn:
        print("Draw")

    if human_turn == "rock" and computer_turn == "scissors":
        print("Human wins")

    elif human_turn == "paper" and computer_turn == "rock":
        print("Human wins")

    elif human_turn == "scissors" and computer_turn == "paper":
        print("Human wins")

    else:
        print("Computer Wins")
    
    restart = input("Wanna play again? Write y or n: ")
    if restart == "y":
        rps()
    else:
        exit
rps()
