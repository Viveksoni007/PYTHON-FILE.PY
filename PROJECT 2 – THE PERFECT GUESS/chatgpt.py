import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        # Ask the user to enter a guess
        user_guess = int(input("Guess the number (between 1 and 100): "))
        number_of_guesses += 1

        # Provide feedback based on the user's guess
        if user_guess > number_to_guess:
            print("Lower number please.")
        elif user_guess < number_to_guess:
            print("Higher number please.")
        else:
            print(f"Congratulations! You guessed the correct number in {number_of_guesses} attempts.")
            break

# Run the guessing game
guess_the_number()
