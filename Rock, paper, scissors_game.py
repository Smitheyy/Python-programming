
import random

options = ("rock", "paper", "scissors")
streak = []
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper. scissors): ")
        print("---------------------------------------------------------------------------------------------------")

    print(f"Player 1 has picked: {player}")
    print(f"Player 2 has picked: {computer}")

    if player == computer:
        print("---------------------------------------------------------------------------------------------------")
        print("It's a tie!")
        print("---------------------------------------------------------------------------------------------------")

    elif player == "scissors" and computer == "paper":
        print("---------------------------------------------------------------------------------------------------")
        print("You win!")
        print("---------------------------------------------------------------------------------------------------")
        streak.append("You win!")

    elif player == "rock" and computer == "scissors":
        print("---------------------------------------------------------------------------------------------------")
        print("You win!")
        print("---------------------------------------------------------------------------------------------------")
        streak.append("You win!")

    elif player == "paper" and computer == "rock":
        print("---------------------------------------------------------------------------------------------------")
        print("You win!")
        print("---------------------------------------------------------------------------------------------------")
        streak.append("You win!")

    else:
        print("---------------------------------------------------------------------------------------------------")
        print("You lose!")
        print("---------------------------------------------------------------------------------------------------")

    play_again = input("Do you wish to play again?(Y/N): ").upper()

    if play_again == "Y":
        print("---------------------------------------------------------------------------------------------------")
        running = True

    elif play_again == "N":

        print("---------------------------------------------------------------------------------------------------")

        if streak.count("You win!") >= 2:
            print("Congratulations your win streak is equivalent to %d :)" % streak.count("You win!"))

        elif streak.count("You win!") == 1:
            print("You've just begun your win streak!")

        else:
            print("---------------------------------------------------------------------------------------------------")
            print("You don' have a win streak...sorry :(")
            print("---------------------------------------------------------------------------------------------------")

        print("Thanks for playing! :)")
        print("---------------------------------------------------------------------------------------------------")

        running = False

    else:
        running = False
        print("Something has gone wrong...")
