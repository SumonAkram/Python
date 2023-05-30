import random
import enum


class PasswordRules(enum.Enum):
    LENGTH = 8
    LETTERS = 3
    NUMBERS = 3
    SPECIAL_CHARS = 2


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        attempts = 0
        while attempts < 3:
            input_password = input("Enter your password: ")
            if input_password == self.password:
                print("Login successful!")
                return True
            else:
                attempts += 1
                print("Invalid password. Please try again.")
        print("Too many login attempts. Exiting...")
        return False


class SecretNumberGame:
    def __init__(self):
        self.user = None
        self.secret_number = None

    def play(self):
        if not self.user:
            print("Please login to play.")
            return
        print(f"Welcome {self.user.username}!")
        user_input = input("Enter three digits: ")
        if not user_input.isdigit() or len(user_input) != 3:
            print("Invalid input. Please enter three digits.")
            return
        user_digits = [int(d) for d in user_input]
        if user_digits == self.secret_number:
            print("Congratulations, you guessed the secret number!")
        else:
            match_count = len(set(user_digits) & set(self.secret_number))
            print(f"{match_count} digits match, but not in the right position.")

    def generate_secret_number(self):
        self.secret_number = random.sample(range(10), 3)
        print("Secret number generated.")


def generate_password() -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    password = ""
    password += "".join(random.choices(letters, k=PasswordRules.LETTERS.value))
    password += "".join(random.choices(numbers, k=PasswordRules.NUMBERS.value))
    password += "".join(random.choices(special_chars, k=PasswordRules.SPECIAL_CHARS.value))
    password = "".join(random.sample(password, len(password)))
    return password


def main():
    password = generate_password()
    print(f"Your password is: {password}")
    username = input("Enter your username: ")
    user = User(username, password)
    if not user.login():
        return
    game = SecretNumberGame()
    game.generate_secret_number()
    game.user = user
    while True:
        game.play()
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() != "y":
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()