import random
import time


# ---------------------------------------------------------
# GLOBAL VARIABLES
# ---------------------------------------------------------

DEFAULT_MIN = 1
DEFAULT_MAX = 100
DEFAULT_ATTEMPTS = 7


# ---------------------------------------------------------
# DISPLAY FUNCTIONS
# ---------------------------------------------------------

def print_line():
    print("-" * 55)


def display_title():
    print_line()
    print("        NUMBER GUESSING GAME")
    print_line()


def display_rules():
    print("\nWelcome to the Number Guessing Game!")
    print("I will select a random number.")
    print("Your job is to guess the number correctly.")
    print("You will receive hints after every wrong guess.")
    print_line()


def display_difficulties():
    print("\nChoose a difficulty level:")
    print("1. Easy   - Numbers 1 to 50, 10 attempts")
    print("2. Medium - Numbers 1 to 100, 7 attempts")
    print("3. Hard   - Numbers 1 to 200, 5 attempts")


def display_menu():
    print("\nMAIN MENU")
    print_line()
    print("1. Start Game")
    print("2. How to Play")
    print("3. Exit")
    print_line()


# ---------------------------------------------------------
# INPUT FUNCTIONS
# ---------------------------------------------------------

def get_menu_choice():
    while True:
        choice = input("Enter your choice: ")

        if choice in ("1", "2", "3"):
            return choice

        print("Invalid choice. Please enter 1, 2, or 3.")


def get_difficulty():
    display_difficulties()

    while True:
        choice = input("\nSelect difficulty: ")

        if choice == "1":
            return 1, 50, 10

        if choice == "2":
            return 1, 100, 7

        if choice == "3":
            return 1, 200, 5

        print("Please select 1, 2, or 3.")


def get_guess(min_number, max_number, attempt, total_attempts):
    while True:
        guess = input(
            f"Attempt {attempt}/{total_attempts} - "
            f"Enter your guess ({min_number}-{max_number}): "
        )

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if guess < min_number or guess > max_number:
            print(
                f"Please enter a number between "
                f"{min_number} and {max_number}."
            )
            continue

        return guess


# ---------------------------------------------------------
# GAME LOGIC
# ---------------------------------------------------------

def check_guess(guess, number):
    if guess == number:
        return "correct"

    if guess < number:
        return "low"

    return "high"


def give_hint(guess, number):
    difference = abs(guess - number)

    if difference <= 5:
        print("Hint: You are VERY close!")

    elif difference <= 15:
        print("Hint: You are close.")

    elif difference <= 30:
        print("Hint: You are getting warmer.")

    else:
        print("Hint: You are quite far away.")


def give_direction(result):
    if result == "low":
        print("Too Low! Try a higher number.")

    elif result == "high":
        print("Too High! Try a lower number.")


def calculate_score(attempt, total_attempts):
    remaining = total_attempts - attempt

    score = 100 + (remaining * 20)

    if score < 20:
        score = 20

    return score


def display_score(score):
    print_line()
    print("Your score:", score)
    print_line()


# ---------------------------------------------------------
# GAME FUNCTION
# ---------------------------------------------------------

def play_game(min_number, max_number, total_attempts):
    number = random.randint(min_number, max_number)

    print("\nI have selected a number.")
    print(
        f"The number is between {min_number} "
        f"and {max_number}."
    )

    print(f"You have {total_attempts} attempts.")
    print()

    attempt = 1

    while attempt <= total_attempts:
        guess = get_guess(
            min_number,
            max_number,
            attempt,
            total_attempts
        )

        result = check_guess(guess, number)

        if result == "correct":
            print("\nCongratulations!")
            print("You guessed the correct number!")
            print(f"You guessed it in {attempt} attempt(s).")

            score = calculate_score(
                attempt,
                total_attempts
            )

            display_score(score)

            return True, score

        give_direction(result)
        give_hint(guess, number)

        remaining = total_attempts - attempt

        if remaining > 0:
            print(
                f"You have {remaining} "
                f"attempt(s) remaining.\n"
            )

        attempt += 1

    print("\nGame Over!")
    print("You used all your attempts.")
    print("The correct number was:", number)
    print("Better luck next time!")

    return False, 0


# ---------------------------------------------------------
# RULES FUNCTION
# ---------------------------------------------------------

def show_how_to_play():
    print_line()
    print("HOW TO PLAY")
    print_line()

    print("1. Choose a difficulty level.")
    print("2. The computer selects a random number.")
    print("3. Enter your guess.")
    print("4. The game tells you if your guess")
    print("   is too high or too low.")
    print("5. You also receive a distance hint.")
    print("6. Guess the number before your attempts")
    print("   run out.")
    print("7. Your score depends on how quickly")
    print("   you find the number.")

    print_line()
    input("Press Enter to return to the menu...")


# ---------------------------------------------------------
# PLAY AGAIN FUNCTION
# ---------------------------------------------------------

def play_again():
    while True:
        choice = input(
            "\nWould you like to play again? (y/n): "
        ).lower()

        if choice == "y":
            return True

        if choice == "n":
            return False

        print("Please enter y or n.")


# ---------------------------------------------------------
# GAME STATISTICS
# ---------------------------------------------------------

def display_statistics(games, wins, total_score):
    print_line()
    print("GAME STATISTICS")
    print_line()

    print("Games played:", games)
    print("Games won:", wins)
    print("Games lost:", games - wins)
    print("Total score:", total_score)

    if games > 0:
        win_rate = (wins / games) * 100
        print(f"Win rate: {win_rate:.1f}%")

    print_line()


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():
    games_played = 0
    games_won = 0
    total_score = 0

    display_title()

    while True:
        display_menu()

        choice = get_menu_choice()

        if choice == "1":
            min_number, max_number, attempts = get_difficulty()

            time.sleep(0.5)

            won, score = play_game(
                min_number,
                max_number,
                attempts
            )

            games_played += 1

            if won:
                games_won += 1
                total_score += score

            display_statistics(
                games_played,
                games_won,
                total_score
            )

            if not play_again():
                print("\nThanks for playing!")
                break

        elif choice == "2":
            show_how_to_play()

        elif choice == "3":
            print("\nThanks for playing!")
            print("Goodbye!")
            break


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":
    main()

