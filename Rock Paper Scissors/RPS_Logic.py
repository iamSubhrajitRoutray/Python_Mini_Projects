import random


ROCK = 0
PAPER = 1
SCISSORS = 2

WIN = "win"
LOSE = "lose"
DRAW = "draw"


def get_computer_choice():
   
    return random.randint(ROCK, PAPER, SCISSORS)


def determine_winner(user_choice, computer_choice):


    if user_choice == computer_choice:
        return DRAW

    if (
        (user_choice == ROCK and computer_choice == SCISSORS)
        
        or (user_choice == PAPER and computer_choice == ROCK)
        
        or (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        return WIN

    return LOSE

