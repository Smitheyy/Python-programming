
def game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for question in questions:
        print("---------------------------------------------------------")
        print(question)
        for answer in answers[question_num - 1]:
            print(answer)

        print("---------------------------------------------------------")
        choice = input("Enter A, B, C or D: ")
        choice = choice.upper()

        guesses.append(choice)
        print("---------------------------------------------------------")
        correct_guesses += check_answer(questions.get(question), choice)  # correct_guesses = correct_guesses + check_answer
        question_num += 1

    display_score(correct_guesses, guesses)
    print("---------------------------------------------------------")


def check_answer(answer, choice):
    if answer == choice:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------------------------------------------")
    print("RESULTS")
    print("---------------------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses / len(questions))*100)
    print(score)


def play_again():

    another_try = input("Do you want to play again?(Type 'Y' for 'Yes' and if not type 'N' for 'No'): ")
    another_try = another_try.upper()

    if another_try == "Y":
        print("---------------------------------------------------------")
        return True
    elif another_try == "N":
        print("---------------------------------------------------------")
        return False
    else:
        print("---------------------------------------------------------")
        print("Please type in only either a letter Y which stands for 'Yes' or a letter N for 'No' ")
        exit()


questions = {"1.Who is responsible for Minecraft's creation?: ": "A",
             "2.When was Minecraft released?: ": "B",
             "3.What is the rarest ore in Minecraft?": "D",
             "4.The main objective of Minecraft is: ": "C",
             "5.What is the name of Minecraft's protagonist?: ": "B"}

answers = [["A.Markus Persson", "B.Scott Cawthon", "C.George Fan", "D.Troy Baker"],
           ["A.2011", "B.2009", "C.2013", "D.2012"],
           ["A.Ancient Debris", "B.Gold", "C.Diamond", "D.Emerald"],
           ["A.To build a house", "B.To kill the wither", "C.To kill the Ender Dragon", "D.To acquire a full netherite gear"],
           ["A.Ted", "B.Steve", "C.John", "D.Bob"]]

game()
while play_again():
    game()

print("Thanks for playing!")
