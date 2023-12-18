import random

options = ("rock", "scisors", "paper")

player = None
computer = random.choice(options)
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options: 
            player = input("Enter an option(rock - paper - scisors): ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
            print("It's a tie")
    elif player == "rock" and computer == "scisors":
            print("You win!")
    elif player == "paper" and computer == "rock":
            print("you win!")
    elif player == "scisors" and computer == "paper":
            print("you win!")
    else:
            print("You lose!")

    play_again = input ("Do you want to play again?(y/n): ").lower()

    if not play_again == "y":
        running = False

print("Tank you for your participation...")




