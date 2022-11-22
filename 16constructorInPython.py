# class Myclass():
#     def Moth(self):
#         print("Hi Machis")
#     def __init__(self): # Use the constructor first pirnt this value
#         print("I Am Raj")
# c=Myclass()#
# c.Moth()
#
#
# ## Converting local variable to class variable
#
# class Myclass():
#     def value(self,val1,val2):
#         print(val1) # local variable
#         print(val2)
#         self.val1=val1 # converting the class variable
#         self.val2=val2
#     def add(self):
#         print(self.val1+self.val2)
# mc=Myclass()
# mc.value(10,15)
# mc.add()
#
# ## construcror method changing in local to class variable
#
# class Myclass():
#     def __init__(self,val1,val2):
#         print(val1) # local variable
#         print(val2)
#         self.val1=val1 # converting the class variable
#         self.val2=val2
#     def add(self):
#         print(self.val1+self.val2)
# mc=Myclass(10,15)
# mc.add()
#
# ## How to call current class method in another method
# class Myclass():
#     def m1(self):
#         print("This is M1 method")
#         self.m2(100) # this is call method in same class another method
#     def m2(self,a):
#         print("This is m2 method",a)
# mc=Myclass()
# mc.m1() # You must use in brackets ***

#
#
# ## Constructor with Arguments
#
# class Myclass():
#     def __init__(self,Name): # Local variables
#         print(Name)
# mc=Myclass("Raj")
#
#
# class Myclass():
#     Name=("Kumar") # class variable
#     def __init__(self,Name): # Local variables
#         print(Name+self.Name) # Possible in concatination
#         print(self.Name)
# mc=Myclass("Raj")
#
#
# #Requirment
# # Class name= Emp
# #Constructor=Eid,Ename,sal
# #Display method= print Eid, Ename, Sal
#
# class Emp():
#     def __init__(self,Eid,Ename,Sal):
#         print(Eid)
#         print(Ename)
#         print(Sal)
# mc=Emp(12345,"Raj",20000) # You not use a Display Method

#
# class Emp():
#     def __init__(self, Eid, Ename, Sal):
#         self.Eid = Eid  # Change Local variable to Class variable
#         self.Ename = Ename
#         self.Sal = Sal
#
#     def display(self):
#         print("EmpID:{} , EmpName:{}, EmpSal:{}".format(self.Eid, self.Ename, self.Sal))  # curly Braces important
#         print("EmpID:%d , EmpName:%s, EmpSal:%d" % (self.Eid, self.Ename, self.Sal))
#
#
# mc = Emp(150911, "Rajkumar", 20150)
# mc.display()


# ### __str__
# class Myclass():
#     pass
# mc=Myclass
# print(mc) #<class '__main__.Myclass'>  This message return in__str__
#
#
# class Myclass():
#     def __str__(self):
#         return ("WELCOME")
# mc=Myclass()
# print(mc) # WELCOME


#Example
#
# class Emp():
#     def __init__(self, Eid, Ename, Sal):
#         self.Eid = Eid  # Change Local variable to Class variable
#         self.Ename = Ename
#         self.Sal = Sal
#
#     def __str__(self):
#         return ("EmpID:{} , EmpName:{}, EmpSal:{}".format(self.Eid, self.Ename, self.Sal))  # curly Braces important
#
#
# mc = Emp(150911, "Rajkumar", 20150)
# print(mc)


##  __del__

class Myclass():
    def __del__(self):
        print("Destroyed")


mc1=Myclass()
mc1.__del__()
mc2=Myclass()
mc2.__del__()
mc3=Myclass()

