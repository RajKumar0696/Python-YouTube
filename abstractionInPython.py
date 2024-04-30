# Created in basic abstract class
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        print("Its passable") # TypeError: Can't instantiate abstract class A with abstract method display

class B():
    def display(self):
        print("This is abstract method")
mc=B()

mc.display()


#------------------------------------------------------------------------
from abc import ABC,abstractmethod
class Bakery(ABC):
    @abstractmethod
    def eat(self):
        print("This is Bakery")
class Cake(Bakery):
    def eat(self):
        print("Very tasty")
class Choco(Bakery):
    def eat(self):
        print("Very Sweet")
class Snaks(Bakery):
    def eat(self):
        print("Very crispy")
mc=Cake()
mc.eat()
mc=Choco()
mc.eat()
mc=Snaks()
mc.eat()
# mc=Bakery()
mc.eat()  # TypeError: Can't instantiate abstract class Bakery with abstract method eat
# cannot be run parent class in abstaction


## One abstract class and more then sub classes
from abc import ABC,abstractmethod
# class X(ABC):# Abstract class
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
# class Y(X):
#     def m1(self):
#         print("This is m1")
# mc=Y()
# mc.m1()   # TypeError: Can't instantiate abstract class Y with abstract method m2

# ----------------------------------------------------------

from abc import ABC, abstractmethod


class X(ABC):  # Abstract class
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class Y(X):
    def m1(self):
        print("This is m1")


class Z(Y):
    def m2(self):
        print("This is m2")


mc = Z()
mc.m1()  # This is m1
mc.m2()  # This is m2

# constructor method in abstraction
from abc import ABC, abstractmethod
class Cal(ABC):
    def __init__(self,value):
        self.value=value
    @abstractmethod
    def add(self):
        print("None")
    @abstractmethod
    def sum(self):
        print("None")
class A(Cal):
    def add(self):
        print(self.value+30)
    def sum(self):
        print(self.value-30)
mc=A(1)
mc.add()
mc.sum()


#_________________________________________________________
from abc import ABC,abstractclassmethod
class A(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def cat(self):
        pass
    @abstractmethod
    def dog(self):
        pass
class B(A):
    def cat(self):
        print("Cat say meow meow")
    def dog(self):
        print("Dog say bow bow")
mc=B()
mc.cat()
mc.dog()

