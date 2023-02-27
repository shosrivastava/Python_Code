print("This code is for Rock, Paper and Scissors game.\n")

from random import randint

game_choices = ["rock", "paper", "scissors"]

while True:
    computer = game_choices[randint(0, 2)]

    player = input("Enter your choice from rock, paper or scissors. Press 'q' to quit the game.\n").lower()

    if player == 'q':
        print("The gamne has ended. Thanks for playing the game.\n")
        break
    elif player == computer:
        print("It's a tie! You and the computer selected the same choice " + computer)

    elif player == 'rock':
        if computer == 'paper':
            print("You loose as computer selected " + computer)
        else:
            print("You win as computer selected " + computer)

    elif player == 'paper':
        if computer == 'scissors':
            print("You loose as computer selected " + computer)
        else:
            print("You win as computer selected " + computer)

    elif player == 'scissors':
        if computer == 'paper':
            print("You win as computer selected " + computer)
        else:
            print("You loose as computer selected " + computer)

    else:
        print("You did not enter the correct choice. Please, try again!\n")