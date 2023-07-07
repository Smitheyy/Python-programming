class Motorcycle:
    wheels = 2

    def __init__(self, module, model, year, color):
        self.module = module
        self.model = model
        self.year = year
        self.color = color

    def motorcycle_details(self):
        print("The brand of the motorcycle is " + self.module)
        print("The model of the motorcycle is " + self.model)
        print("This motorcycle was made in %d" % self.year)
        print("This motorcycle is " + self.color + " in color")

    def wheel_count(self):
        print("This motorcycle has %d wheels" % self.wheels)