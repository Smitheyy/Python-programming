class Animal:
    alive = True

    @staticmethod
    def eat():
        print("Animals can eat.")

    @staticmethod
    def slumber():
        print("Animals can sleep.")

    @staticmethod
    def drink():
        print("Animals can drink")

    @staticmethod
    def sing():
        print("Some animals can sing")

    @staticmethod
    def fly():
        print("Some animals can fly")


class Insect(Animal):

    @staticmethod
    def fly():
        print("Insects can fly")

    @staticmethod
    def sting():
        print("Insects can sting")


class Mosquito(Insect):

    @staticmethod
    def eat():
        Animal().eat()
        print("Mosquitoes suck blood out of its victims")

    @staticmethod
    def fly():
        Insect().fly()
        print("Mosquitoes can fly")


class Mammal(Animal):

    @staticmethod
    def fur():
        print("Mammals have fur")

    @staticmethod
    def slumber():
        print("Mammals can slumber")


class Dog(Mammal):

    @staticmethod
    def fur():
        Mammal().fur()
        print("Dogs have fur")

    @staticmethod
    def slumber():
        Animal().slumber()
        print("Dogs can slumber")


class Fish(Animal):

    @staticmethod
    def swim():
        print("Fishes can swim")

    @staticmethod
    def drink():
        print("Fishes can drink")


class Salmon(Fish, Animal):

    @staticmethod
    def swim():
        Fish().swim()
        print("Salmons can swim")

    @staticmethod
    def drink():
        Animal().drink()
        Fish().drink()
        print("Salmons drink water")


class Bird(Animal):

    @staticmethod
    def fly():
        print("Birds can fly")

    @staticmethod
    def sing():
        print("Birds can sing")


class Sparrow(Bird, Animal):
    @staticmethod
    def sing():
        Animal().sing()
        Bird().sing()
        print("Sparrows can sing")

    @staticmethod
    def fly():
        Animal().fly()
        Bird().fly()
        print("Sparrows can fly")


class Pigeon(Sparrow):

    @staticmethod
    def fly():
        Animal().fly()
        Bird().fly()
        Sparrow().fly()
        print("Pigeons can fly and they are annoying")


animal = Animal()
insect = Insect()
mammal = Mammal()
fish = Fish()
bird = Bird()
mosquito = Mosquito()
dog = Dog()
salmon = Salmon()
sparrow = Sparrow()
pigeon = Pigeon()

animal.eat()
print("---------------------------------------------------------------------------------------------------------------")
insect.fly()
print("---------------------------------------------------------------------------------------------------------------")
mosquito.fly()
mosquito.eat()
print("---------------------------------------------------------------------------------------------------------------")
mammal.fur()
print("---------------------------------------------------------------------------------------------------------------")
dog.fur()
print("---------------------------------------------------------------------------------------------------------------")
Fish.swim()
print("---------------------------------------------------------------------------------------------------------------")
salmon.swim()
print("---------------------------------------------------------------------------------------------------------------")
Bird.fly()
Bird.sing()
print("---------------------------------------------------------------------------------------------------------------")
sparrow.fly()
sparrow.sing()
print("---------------------------------------------------------------------------------------------------------------")
pigeon.fly()
pigeon.sing()
pigeon.eat()
print("---------------------------------------------------------------------------------------------------------------")

# it is called multi-level inheritance
# there is also multiple inheritance (u write a coma and that's it)
# there is method overriding (an object will use sth more closely related to it, and it will ignore the "mother class")
# we have sth called method chaining ()
# if I want to call out the parent function I should type 'the name of the class' or super()."the name of the function"
# inside of class.
