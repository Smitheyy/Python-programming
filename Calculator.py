def sum_up(x, y):
    return x + y


def substract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


number_1 = float(input("Choose the first number: "))
number_2 = float(input("Choose the second number: "))

print("Choose an action: ")
print("1.sum_up")
print("2.substract")
print("3.multiply")
print("4.divide")

choice = input("Which operation would you like to pick? (choose 1, 2, 3 or 4): ")

if choice == "1":
    print(number_1, "+", number_2, "=", sum_up(number_1, number_2))

elif choice == "2":
    print(number_1, "-", number_2, "=", substract(number_1, number_2))

elif choice == "3":
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif choice == "4":
    print(number_1, ":", number_2, "=", divide(number_1, number_2))

else:
    print("Error!")
