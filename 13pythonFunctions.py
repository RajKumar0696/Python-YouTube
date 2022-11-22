def myfun():
    print(myfun())

def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    print(result)
sum(5,20)

#RETURN VALUES

def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    return result
s=sum(5,20)
print(s)