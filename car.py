class Car:
    wheels = 4  # class variable

    def __init__(self, module, model, year, color):     # this command is an object creator.
        self.module = module
        self.model = model  # these variables are called instance variables.
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.module+" is driving.")

    def stop(self):
        print("This "+self.module+" is stopped.")
