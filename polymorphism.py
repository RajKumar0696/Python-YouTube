# Polymorphism overriding  variables
class Parent:
    Name = "Raj"


class Child(Parent):
    Name = "Kumar"


mc = Child()
print(mc.Name)  # Kumar

mc = Parent()
print(mc.Name)


# polymorphism overriding methods
class Bank:
    def Rate_of_intrest(self):
        return 24


class Axis(Bank):  # Overriding the same method
    def Rate_of_intrest(self):
        return 20


mc = Axis()
print(mc.Rate_of_intrest())  # 20

mc = Bank()
print(mc.Rate_of_intrest())  # 24


# Overloading Methods in polymorphism
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello", name)
        else:
            print("Hello ")


mc = Human()
mc.sayHello()


# __________________________________________
class Bird():
    def Fly(self, Name=None):
        if Name == "Crow":
            print("Can Fly")
        if Name == "Cow":
            print("Cannot Fly")
        if Name is None:
            print("This is SuperHero")


obj = Bird()
obj.Fly("Cow")

from abc import ABC,abstractmethod
class name(ABC):
    @abstractmethod
    def dis(self):
        print("abstract")
obj = name()
obj.dis()
