from car import Car
from motorcycle import Motorcycle
from trike import Trike


def try_again():
    again = input("Do you wish to start again?(Enter Y or N): ")
    again = again.upper()

    while not again:
        again = input("Do you wish to start again?(Enter Y or N): ")
    if again == "Y":
        return True
    elif again == "N":
        print("---------------------------------------------------------------------------------------------------")
        print("Thank you for typing in your answers, I hope you had a great time :)")
        exit()

    else:
        print("Please enter only Y if you agree or N if you want to terminate the program", end=" "
                "(this also additional spaces)")
        print(".")
        print("---------------------------------------------------------------------------------------------------")
        exit()


running = True
vehicle = None

while running:
    try:
        wheels = int(input("Enter the number of wheels your vehicle is supposed to have: "))
        print("---------------------------------------------------------------------------------------------------")

        if wheels == Car.wheels:
            print("This is an ordinary car")
            print("---------------------------------------------------------------------------------------------------")

            module1 = str(input("Enter the brand responsible for the car's construction: "))
            model1 = str(input("Enter the model of the car: "))
            year1 = int(input("Enter the year in which the car was created: "))
            color1 = str(input("Enter the color of the car: "))

            print("---------------------------------------------------------------------------------------------------")

            vehicle = Car(module1, model1, year1, color1)

            vehicle.car_details()

        elif wheels == Motorcycle.wheels:
            print("This is a motorcycle")
            print("---------------------------------------------------------------------------------------------------")

            module1 = str(input("Enter the brand responsible for the motorcycle's construction: "))
            model1 = str(input("Enter the model of the motorcycle: "))
            year1 = int(input("Enter the year in which the motorcycle was created: "))
            color1 = str(input("Enter the color of the motorcycle: "))
            print("---------------------------------------------------------------------------------------------------")

            vehicle = Motorcycle(module1, model1, year1, color1)

            vehicle.motorcycle_details()

        elif wheels == Trike.wheels:
            print("This is a trike - which is a three-wheeled car that can be more maneuverable than", end=" "
                  "traditional four-wheeled cars because it has a smaller turning radius")
            print(".")
            print("---------------------------------------------------------------------------------------------------")

            module1 = str(input("Enter the brand responsible for the trike's construction: "))
            model1 = str(input("Enter the model of the trike: "))
            year1 = int(input("Enter the year in which the trike was created: "))
            color1 = str(input("Enter the color of the trike: "))
            print("---------------------------------------------------------------------------------------------------")

            vehicle = Trike(module1, model1, year1, color1)

            vehicle.trike_details()

        else:
            print("The vehicle is not a car nor a motorcycle nor a trike")
            print("---------------------------------------------------------------------------------------------------")
            exit()

    except ValueError as k:
        print("Please write the number of wheels and years as a digit")
        print("---------------------------------------------------------------------------------------------------")
        print(k)
        exit()

    finally:
        pass

    try_again()
    print("---------------------------------------------------------------------------------------------------")
