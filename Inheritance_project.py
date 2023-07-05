# Try having some fun with the code. Please read about "Method override" and implement some overrides that would benefit the program

class Animal:
    alive = True

    @staticmethod
    def eat():
        print("This animal is eating.")

    @staticmethod
    def slumber():
        print("This animal is sleeping.")


class Mosquito(Animal):

    @staticmethod
    def fly():
        print("This mosquito is flying.")


class Cat(Animal):

    @staticmethod
    def meowing():
        print("This cat is meowing.")


class Dog(Animal):

    @staticmethod
    def bark():
        print("This dog is barking.")


class Salmon(Animal):

    @staticmethod
    def swim():
        print("This salmon is swimming.")


class Sparrow(Animal):

    @staticmethod
    def flying():
        print("This sparrow is flying.")


mosquito = Mosquito()
cat = Cat()
dog = Dog()
salmon = Salmon()
sparrow = Sparrow()

mosquito.fly()
cat.meowing()
dog.bark()
salmon.swim()
sparrow.flying()


# it is called multi-level inheritance
# there is also multiple inheritance (u write a coma and that's it)
# there is method overriding (an object will use sth more closely related to it, and it will ignore the "mother class")
# we have sth called method chaining ()
