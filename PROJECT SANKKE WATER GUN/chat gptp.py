import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def snake_water_gun_game():
    choices = ['snake', 'water', 'gun']
    computer_choice = random.choice(choices)

    print("Welcome to the Snake, Water, Gun game!")
    print("Please choose: snake, water, or gun")

    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose from 'snake', 'water', or 'gun'.")
        return

    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
snake_water_gun_game()
