## Basic Function Creation
"""def myfunction():
    pass


myfunction()

## Create a Function

def sum(start,end):
    result=0
    for i in range(start,end+1): #10+1,11+1,12+1 ........29+1 === 420
        result=result+i
    print(result)
sum(10,30)


## Functions Return Value

def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    return result
S=sum(10,30) # you want some return value you must save the function into the Variable
print(S)


## Function Return Function Without Some Value

def sum(start,end):
    if (start>end):
        print("Star in Big Number")
        return  # Python Function You dot need input in Return value its always none
    result=0
    for i in range(start,end+1):
        result=result+i
    return result

s=sum(40,30)
print(s)


# Passing Arguments positional value
def myfun(a,b=100):
    print(a,b)
myfun(10) #10,100
myfun(10,20) # re assing the b value"""

# # Keywords arguments
# def savi(message,name):
#     print(message+"",name)
#
#
# savi("va machi","Rajuuu") # this is positional arguments
# savi(message="vada thambbi",name="Rajkumar") # keyword arguments
# savi(name="Rockey",message="vanakam")
#
# # positional arguments and keyword arguments
# def myfun(a,b,c,d):
#     print(a,b,c,d)
#
#
# myfun(10,20,30,40)# positional arguments
# myfun(10,b=20,c=30,d=40) # positional arguments and keyword arguments
# myfun(c=30,b=20,d=40,a=10)
# myfun(a=20,b=40,c=87,d=76)


# Returning Multiple Value from Function
def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a


b=bigger(101,20)
print(b)
print(type(b)) # <class 'tuple'>




