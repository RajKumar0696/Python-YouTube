# Encapsulation in PRIVATE Variable

class MyClass:
    __a = 100  # Private Variable

    def display(self):
        print(self.__a)


mc = MyClass()
mc.display()


class MyClass:
    __raj = 10
    __kumar = 30

    def add(self):
        print(self.__raj + self.__kumar)


mc = MyClass()
mc.add()


# Encapsulation in PRIVATE Method

class MyClass():
    def __Display1(self):
        print("This is Display1 Method and Private Method")

    def Display2(self):
        print("This is Display2 Method Public Method")
        self.__Display1()


mc = MyClass()


# mc.Display1() # can't be run private method in out of class


# We can access private variable in outside of class indirectly method

class MyClass():
    __empid = 150911

    def getempid(self, empid):
        self.__empid = empid  # private variable assing the value in public variable

    def display(self):
        print(self.__empid)


mc = MyClass()
mc.getempid(105)  # value change the private variable
mc.display()


class MyClass():
    __NumberofEmp = 142

    def NumberofDCEmp(self, DCEmp):
        self.__NumberofEmp = DCEmp

    def Overallemp(self):
        print(self.__NumberofEmp)


mc = MyClass()
mc.NumberofDCEmp(25)
mc.Overallemp()
