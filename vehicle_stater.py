def try_again():

    again = input("Do you wish to start again?(Enter Y or N): ")
    again = again.upper()

    if again == "Y":
        return True
    elif again == "N":
        print("-------------------------------------------------------------------------------------------------------")
        print("Thank you for typing in your answers, I hope you had a great time :)")
        exit()

    else:
        print("Please enter only Y if you agree or N if you want to terminate the program")
        exit()


# ------------------------------------------------------------------------

running = True

while running:

    try:
        wheels = int(input("Enter the number of wheels that the vehicle is supposed to have: "))
        print("-------------------------------------------------------------------------------------------------------")
        module = str(input("Enter the brand responsible for the vehicle's construction: "))
        print("-------------------------------------------------------------------------------------------------------")
        model = str(input("Enter the model of the vehicle: "))
        print("-------------------------------------------------------------------------------------------------------")
        year = int(input("Enter the year in which vehicle was created: "))
        print("-------------------------------------------------------------------------------------------------------")
        color = str(input("Enter the color of the vehicle: "))
        print("-------------------------------------------------------------------------------------------------------")
    except ValueError as p:
        print("Please enter only the number of wheels and the year of your car's creation as a digit, thanks :)")
        print(p)
        print("-------------------------------------------------------------------------------------------------------")
        exit()
# ------------------------------------------------------------------------
    print("Your vehicle has "+str(wheels)+" wheels")
    print("The brand of your vehicle is "+module)
    print("The model of your vehicle is "+model)
    print("Your vehicle was created in "+str(year))
    print("Your vehicle is "+color+" in color")
    print("-------------------------------------------------------------------------------------------------------")
# ------------------------------------------------------------------------
    try_again()
