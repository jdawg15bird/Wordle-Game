
import random

# picks a random word
def choose_word():
    words = ["plant", "house", "brick", "stone", "chair", "grape", "flame", "table"]
    word = random.choice(words)
    return word


# makes sure the guess works
def get_guess(previous_guesses):
    guess = input("Enter a five-letter word: ").lower()

    while len(guess) != 5 or not guess.isalpha() or guess in previous_guesses:
        if len(guess) != 5:
            print("You need to enter 5 letters.")
        elif not guess.isalpha():
            print("Only enter letters.")
        else:
            print("You already guessed that word.")

        guess = input("Enter a five-letter word: ").lower()

    return guess


# checks each letter in the guess
def evaluate_guess(guess, secret_word):
    feedback = []

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("G")
        elif guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback


# prints the guess and results
def display_guess(guess, feedback):
    print("Guess:", " ".join(guess.upper()))
    print("Feedback:", " ".join(feedback))


# checks if the player guessed the word
def has_won(guess, secret_word):
    if guess == secret_word:
        return True
    else:
        return False
