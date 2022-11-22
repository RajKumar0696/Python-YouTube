# Polumorphism overriding  variables
class Parent():
    Name="Raj"
class Child(Parent):
    Name="Kumar"
mc=Child()
print(mc.Name) #Kumar

mc=Parent()
print(mc.Name)

#polymorphism overriding methods
class Bank():
    def Rateofintrest(self):
        return 24
class Axis(Bank): ## Overriding the same method
    def Rateofintrest(self):
        return 20
mc=Axis()
print(mc.Rateofintrest()) #20

mc=Bank()
print(mc.Rateofintrest()) #24


#Overloading Methods in polymorphism
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello",name)
        else:
            print("Hello ")


mc = Human()
mc.sayHello()





#__________________________________________
class Bird():
    def Fly(self,Name=None):
        if Name=="Crow":
            print("Can Fly")
        if Name=="Cow":
            print("Cannot Fly")
        if Name is None:
            print("This is SuperHero")


mc=Bird()
mc.Fly("Cow")