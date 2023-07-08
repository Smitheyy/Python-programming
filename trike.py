class Trike:
    wheels = 3

    def __init__(self, module, model, year, color):     # this command is an object creator.
        self.module = module
        self.model = model  # these variables are called instance variables.
        self.year = year
        self.color = color

    def trike_details(self):
        print("The brand of the trike is %s" % self.module)
        print("The model of the trike is %s" % self.model)
        print("This trike was made in %d" % self.year)
        print("This trike is %s in color" % self.color)
        print("-------------------------------------------------------------------------------------------------------")
