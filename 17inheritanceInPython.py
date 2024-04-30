# # Basic Example in Inheritance
#
# class A():
#     def m1(self):
#         print("This is m1 method class A")
# class B(A):
#     def m2(self):
#         print("This is m2 method class B")
# mc=A()
# mc.m1()
#
# mc2=B()
# mc2.m2()
#
# ## Single Inheritance (one parent and one child)
# class A():
#     a,b=30,40
#     def m1(self):
#         print(self.a+self.b)
# class B(A): # Class B extension the Class A
#     c,d=50,60
#     def m2(self):
#         print(self.c+self.d)
# mc=B()
# mc.m1() #70 (m1 class is A. This is meaning of B(A)
# mc.m2() #110

#
#
# ## MultiLevel Inheritance (one parent and more than one child)
# class A():
#     a,b=30,40
#     def m1(self):
#         print(self.a+self.b)
# class B(A): # Class B extension the Class A
#     c,d=50,60
#     def m2(self):
#         print(self.c+self.d)
# class C(B):
#     e,f=70,80
#     def m3(self):
#         print(self.e+self.f)
#
# mc=B()
# mc.m1()
# mc.m2()
#
# mc=C()
# mc.m1()
# mc.m2()
# mc.m3()


### Hierertical Inheritance (one parent and tow child)
# class A():
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     c,d=30,40
#     def m2(self):
#         print(self.c+self.d)
# class C(A):
#     e,f=50,60
#     def m3(self):
#         print(self.e+self.f)
# mc=B()
# mc.m1()
# mc.m2()
#
# mc=C()
# mc.m1()
# mc.m3()
#
## Multiple Inheritance (one child and multiple parents)
class A():
    a,b=10,20
    def m1(self):
        print(self.a+self.b)
class B():
    c,d=30,40
    def m2(self):
        print(self.c+self.d)
class C(A,B):
    e,f=50,60
    def m3(self):
        print(self.e+self.f)
mc=C()
mc.m1()
mc.m2()
mc.m3()
