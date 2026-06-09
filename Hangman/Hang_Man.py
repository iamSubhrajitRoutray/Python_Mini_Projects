import random
from Hangman_Words import word_list
from Hangman_Art import logo, stages



def play_game():
    
    chosen_word = random.choice(word_list)
    # print(chosen_word)

    placeholder = ""

    word_length = len(chosen_word)

    placeholder = "_" * word_length
    print(placeholder)

    correct_letters = []

    lives = 6
    
    game_over = False

    while not game_over:

        guess = input("Guess a letter : ").lower()

        display = ""
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in correct_letters:

            print("You have already guess this letter.")
            continue
        

        if guess not in chosen_word:
            lives -= 1
            
            print(f"Oops! Wrong guess! Lives remaining : {lives}/6")
            print(stages[lives])

            if lives == 0:
                print(f"You LOSE! The word is : {chosen_word}")
                game_over = True
                continue
        
        if guess in chosen_word:
            correct_letters.append(guess)
        
        display = ""


        for letter in chosen_word:
            if letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)


        if "_" not in display:
            print("Hurray! You WIN!")
            game_over = True


def main():
    
    print(logo)

    while True:
        play_game()
        
        play_again = input("Would you like to play again ? (yes/no) : ").lower()
        
        if play_again != "yes":
            print("Thanks for playing!")
            break

main()
