# #Super() inheritance way to calling methon
class A():
    def m1(self):
        print("This is m1 method class A")
class B(A):
    def m2(self):
        print("This is m2 method class B")
        super().m1() # This is parent calling method
mc=B()
mc.m2()

#calling parent in variable
class A():
    a,b=10,20
class B(A):
    c,d=30,40
    def m1(self,e,f):
        print(e+f) #local
        print(self.a+self.b) #Child Class
        print(self.c+self.d) # Parent Class
mc=B()
mc.m1(50,60)


# Same variable name calling parents
a,b=70,80
class A():
    a,b=10,20
class B(A):
    a,b=30,40
    def m1(self,a,b):
        print(a+b) #local
        print(self.a+self.b) #Child Class
        print(super().a+super().b) # Parent Class
        print(globals() ["a"]+globals() ["b"]) #global class

mc=B()
mc.m1(50,60)


# Calling Parent in constructor
class A():
    def __init__(self):
        print("This is constructor class A ")
class B(A):
    pass
mc=B() # no constructor in child class printed parent class
#__________________________________________________________________

class A():
    def __init__(self):
        print("This is constructor class A ")
class B(A):
    def __init__(self):
        print("This is constructor class B")
mc=B() # This is constructor class B (print in child class)

#_________________________________________________________________
class A():
    def __init__(self):
        print("This is constructor class A ")
class B(A):
    def __init__(self):
        print("This is constructor class B")
        super().__init__() # both are printed this is parent Constructor # First approach
        A.__init__(self) # Second approach                               _________________
mc=B()                    #__________________
