import random

def play_snake_water_gun():
    print("Snake - Water - Gun")
    n = int(input("Enter the number of rounds: "))
    options = ['s', 'w', 'g']
    rounds = 1
    user_win = 0
    comp_win = 0

    while rounds <= n:
        print(f"Round {rounds}:")
        print("Snake - 's'\nWater - 'w'\nGun - 'g'")
        try:
            player = input("Choose your option: ")
        except EOFError as e:
            print(e)
            continue

        if player not in options:
            print("Invalid input, try again.\n")
            continue

        computer = random.choice(options)

        if computer == 's':
            if player == 'w':
                comp_win += 1
            elif player == 'g':
                user_win += 1
        elif computer == 'w':
            if player == 'g':
                comp_win += 1
            elif player == 's':
                user_win += 1
        elif computer == 'g':
            if player == 's':
                comp_win += 1
            elif player == 'w':
                user_win += 1

        rounds += 1

    if user_win > comp_win:
        print("Congratulations!! You Won 🎉")
    elif comp_win > user_win:
        print("You lose!! 😢")
    else:
        print("Match Draw!! 🤝")

play_snake_water_gun()
