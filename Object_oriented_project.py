from car import Car
from motorcycle import Motorcycle

car_1 = Car("Ford", "Fiesta", 2019, "black")
car_2 = Car("Dacia", "Duster", 2017, "white")
motorcycle = Motorcycle("Honda", "Gold Wing", 2022, "red")

car_1.wheel_count()
car_1.car_details()
print("---------------------------------------------------------")
car_2.wheel_count()
car_2.car_details()
print("---------------------------------------------------------")
motorcycle.wheel_count()
motorcycle.motorcycle_details()
