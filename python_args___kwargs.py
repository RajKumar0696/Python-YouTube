##  *args in python

def sum(*args):
    s=0
    for i in args:
        s+=i
    print("sum is",s)
sum(10,20,30,40)



def mul(a,b,c,d):
    print(a,b,c,d)
arg=(10,20,30,40)
print(*arg)



## **kwargs in python

def MyThree(a,b,c):
    print(a,b,c)
arg={'a':10,'b':20,'c':30}
MyThree(**arg)



def MyThree(**raj):
    for a,b in raj.items():
        print(a,b)
MyThree(Name='Rockey',Study='Python',Salary='10000')


