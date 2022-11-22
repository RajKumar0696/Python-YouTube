# Passing sigle variable
x=lambda a:a+10
print(x(5)) # 15

# passing multiple variables

x=lambda a,b,c:(a+b*c)
print(x(10,5,6)) # 40

x=lambda a,b,c,d,e,f:(a+b*c-d+e*f)
print(x(10,20,30,40,50,60)) #3570

