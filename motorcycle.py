class Motorcycle:
    wheels = 2

    def __init__(self, module, model, year, color):
        self.module = module
        self.model = model
        self.year = year
        self.color = color

    def motorcycle_details(self):
        print("The brand of the motorcycle is %s" % self.module)
        print("The model of the motorcycle is %s" % self.model)
        print("This motorcycle was made in %d" % self.year)
        print("This motorcycle is %s in color" % self.color)
        print("-------------------------------------------------------------------------------------------------------")
