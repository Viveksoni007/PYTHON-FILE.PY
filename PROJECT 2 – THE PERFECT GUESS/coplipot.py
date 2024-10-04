import random

def guess_the_number():
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess < secret_number:
            print("Higher number, please.")
        elif user_guess > secret_number:
            print("Lower number, please.")
        else:
            print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
