
from wordle_functions import *

print("Welcome to Mystery Wordle!")
print("Try to guess the 5 letter word.")
print("G = right letter and right spot")
print("Y = right letter but wrong spot")
print("- = letter is not in the word")

play_again = "yes"

while play_again == "yes":

    secret_word = choose_word()
    previous_guesses = []
    won = False

    for attempt in range(1, 7):
        print()
        print("Attempt", attempt, "of 6")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("Congratulations! You guessed the word!")
            won = True
            break

    if won == False:
        print("You ran out of guesses.")
        print("The word was:", secret_word)

    print()
    play_again = input("Would you like to play again? yes/no: ").lower()

print("Thanks for playing!")
