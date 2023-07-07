class Car:
    wheels = 4  # class variable

    def __init__(self, module, model, year, color):     # this command is an object creator.
        self.module = module
        self.model = model  # these variables are called instance variables.
        self.year = year
        self.color = color

    def car_details(self):
        print("The brand of the car is "+self.module)
        print("The model of the car is "+self.model)
        print("This car was made in %d" % self.year)
        print("This car is "+self.color+" in color")

    def wheel_count(self):
        print("This car has %d wheels" % self.wheels)
