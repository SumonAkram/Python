import random

def hangman():
    words = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the letters to complete the word. You have 6 attempts.")

    while True:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"

        print("Current word:", hidden_word)

        if hidden_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        if attempts == 0:
            print("You're out of attempts. The word was:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempt(s) left.")

hangman()
