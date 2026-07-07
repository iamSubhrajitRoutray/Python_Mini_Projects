from RPS_Art import game_images

from RPS_Logic import (
    get_computer_choice,
    determine_winner,
    WIN,
    LOSE,
    DRAW,
)

player_score = 0
computer_score = 0
draw_score = 0


def show_banner():
    
    print("============= 'ROCK' : 'PAPER' : 'SCISSORS' ==============")
  


def get_user_choice():

    while True:

        try:

            choice = int(input("\nChoose your weapon\n 0 = Rock\n 1 = Paper\n 2 = Scissors\n Enter your choice: "))

            if choice in [0, 1, 2]:
                return choice

            print("Please enter only 0, 1 or 2.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def display_choice(player, choice):

    print(f"{player} chose:\n")
    print(game_images[choice])


def display_result(result):

    if result == WIN:
        print("🎉 Congratulations!")
        print("You Win!")

    elif result == LOSE:
        print("💻 Computer Wins!")
        print("You Lose!")

    else:
        print("🤝 It's a Draw!")


def update_score(result):

    global player_score
    global computer_score
    global draw_score

    if result == WIN:
        player_score += 1

    elif result == LOSE:
        computer_score += 1

    else:
        draw_score += 1


def display_scoreboard():

    print("========== SCOREBOARD ==========")
    print(f"Player Wins   : {player_score}")
    print(f"Computer Wins : {computer_score}")
    print(f"Draws         : {draw_score}")
    print("=" * 32)


def play_round():

    user_choice = get_user_choice()

    display_choice("You", user_choice)

    computer_choice = get_computer_choice()

    display_choice("Computer", computer_choice)

    result = determine_winner(user_choice, computer_choice)

    display_result(result)

    update_score(result)

    display_scoreboard()


def play_again():

    while True:

        answer = input("Play Again? (Yes/No): ").strip().lower()

        if answer == "yes":
            return True

        if answer == "no":
            return False

        print("Please enter Yes or No.")


def main():

    show_banner()

    while True:

        play_round()

        if not play_again():
            break

    print("\nFinal Score")
    display_scoreboard()
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()