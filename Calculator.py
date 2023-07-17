while True:

    def sum_up(x, y):
        return x + y


    def substract(x, y):
        return x - y


    def divide(x, y):
        if y == 0:
            print("You can't divide by zero...dumbass!")
            exit()
        return x / y


    def multiply(x, y):
        return x * y


    def calculate_again():
        try:
            calculate = input("Do you want to use the calculator again?(type Y or N): ").upper()

            if calculate == "Y":
                return True

            elif calculate == "N":
                print("Thank you for using my calculator, please have a nice day! :)")
                exit()

        except ValueError as k:
            print("Enter only the choices given not numbers!")
            print(k)
            exit()


    try:
        number_1 = float(input("Choose the first number: "))
        number_2 = float(input("Choose the second number: "))

    except ValueError as n:
        print("Enter numbers only!")
        print(n)
        exit()

    finally:
        pass

    print("Choose an action: ")
    print("1.sum_up")
    print("2.substract")
    print("3.multiply")
    print("4.divide")

    try:
        choice = int(input("Which operation would you like to pick? (choose 1, 2, 3 or 4): "))

        if choice == 1:
            print(number_1, "+", number_2, "=", sum_up(number_1, number_2))

        elif choice == 2:
            print(number_1, "-", number_2, "=", substract(number_1, number_2))

        elif choice == 3:
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))

        elif choice == 4:
            print(number_1, ":", number_2, "=", divide(number_1, number_2))

    except ValueError as p:
        print("Enter numbers only!")
        print(p)
        calculate_again()
