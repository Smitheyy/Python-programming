from car import Car

car_1 = Car("Ford", "Fiesta", 2019, "black")
car_2 = Car("Dacia", "Duster", 2017, "white")
motorcycle = Car("Honda", "Gold Wing", 2022, "red")

print(car_1.module)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("This car has "+str(Car.wheels)+" wheels")

car_1.drive()
car_1.stop()
# ----------------------------------------------------------------
print("--------------------------")

print(car_2.module)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print("This car has "+str(Car.wheels)+" wheels")

car_2.drive()
car_2.stop()
# ----------------------------------------------------------------
print("--------------------------")
motorcycle.wheels = 2

print(motorcycle.module)
print(motorcycle.model)
print(motorcycle.year)
print(motorcycle.color)

print("This car has "+str(motorcycle.wheels)+" wheels")

motorcycle.drive()
motorcycle.stop()
