class Myclass:
    def Myfunc(self):
        pass

    def display(self, name):
        print("name is:", name)


mc = Myclass()
mc.Myfunc()
mc.display("Rajkumar")


#
#
#
class Myclass:
    def Myfunc(self):
        pass

    def display(self, workplace):
        print("My Work Place Is:", workplace)


mc = Myclass()
mc.Myfunc()
mc.display("Home")


#
# ######## Instance Method And Static Method
#
class Myclass:
    def Myfunc(self):  ## instance method you use self key word
        print("This is Instance Method")

    @staticmethod
    def Myfunc2():  # static method you don't use self key word
        print("This Is Static Method")


mc = Myclass()
mc.Myfunc()
mc.Myfunc2()


class Myclass:
    def Myfunc(self):  ## instance method you use self key word
        print("This is Instance Method")

    @staticmethod
    def Myfunc2(self):  # static method you dont use self key word
        print(self)


mc = Myclass()
mc.Myfunc()
mc.Myfunc2(10)


# ### Dclaring Variables inside the Class
# class Myclass:
#     a,b=100,200 # this is class variables
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc=Myclass()
# mc.add()
# mc.mul()
#
#
# ### Local , class and global variables
# a,b=10,20 # global variable
# class Myclass:
#     c,d=100,200
#     def add(self,e,f):
#         print(e+f)# Directly Use to LOcal variable
#         print(self.c+self.d)
#         print(a+b)
# mc= Myclass()
# mc.add(10,30)
#
#
# ## ### Local , class and global variables with a same name

a,b=10,20 # global variable
class Myclass:
    a,b=100,200
    def add(self,a,b):
        print(a+b)# Directly Use to LOcal variable
        print(self.a+self.b)
        print(globals()['a']+globals()['b']) # you put a+b its treated local variable
mc= Myclass()                                 #(globals()['a']+globals()['b']) this is current
mc.add(10,30)
#
#
# ## Create Multiple object for one class
# class Myclass:
#     def display(self):
#         print("Good Morning")
# obj1=Myclass()
# obj1.display()
#
# obj2=Myclass()
# obj2.display()
#
# obj3=Myclass()
# obj3.display()
#
#
# #### Named object and nameless Object
#
# class Myclass:
#     def display(self):
#         print("Good Evening")
#
#
# obj1 = Myclass()
# obj1.display() # Named Object
#
# Myclass().display() # Nameless Object


### Memory Location Checking

## Create Multiple object for one class
class Myclass:
    def display(self):
        print("Good Morning")


obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj1 = obj3
obj3 = obj2

print(id(obj1))
print(id(obj2))
print(id(obj3))

print(obj1 is obj2)

print(obj1 is not obj2)
