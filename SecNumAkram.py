from random import randint

def play_game() -> None:
    min_num:int = 1
    max_num:int = 5
    secret_number = randint(min_num, max_num)

    print(f"Guess the secret number between {min_num} and {max_num}")

    while True:
        try:
            user_guess = int(input("Guess please: "))
            if user_guess < min_num or user_guess > max_num:
                print(f"Your guess should be between {min_num} and {max_num}")
            elif user_guess == secret_number:
                print("Congratulations! You guessed the secret number.")
                break
            elif user_guess < secret_number:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            play_game()
            #break
        elif play_again.lower() == "n":
            print("Thanks for playing!")
            #break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

play_game()
