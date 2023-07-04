import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper. scissors): ")

    print(f"Player: {player}")
    print(f"Player: {computer}")

    if player == computer:
        print("It's a tie!")

    elif player == "scissors" and computer == "paper":
        print("You win!")

    elif player == "rock" and computer == "scissors":
        print("You win!")

    elif player == "paper" and computer == "rock":
        print("You win!")

    else:
        print("You lose!")

    play_again = input("Play again?(Y/N): ").upper()

    if play_again == "Y":
        running = True
    elif play_again == "N":
        running = False
        print("Thanks for playing!")
    else:
        running = False
        print("Error!")

