#concatination

num1=input("Enter First Number:") # 10 treate a string
num2=input("Enter Second Number:")# 20 treate a string
print(num1+num2)

# Type casting

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
print(num1+num2)

#Type casting 2

num1=input("Enter First Number:")
num2=input("Enter Second Number:")
print(int(num1)+int(num2))



# Type casting float values


num1=input("Enter First Desimal Number:") #10.5
num2=input("Enter Second Desimal Number:")# 10.5
print(float(num1)+float(num2)) # 21.0


# Type Casting Float and integer value

num1=input("Enter First Desimal Number:")# 10.5
num2=input("Enter Second Desimal Number:")# 10.5  ValueError: invalid literal for int
print(float(num1)+int(num2))


# Type Casting Float and integer value 2

num1=input("Enter First Desimal Number:") #10.5
num2=input("Enter Second NonDesimal Number:")#10
print(float(num1)+int(num2))#20.5


#Type Casting Float and integer(float) value 2

num1=input("Enter First Desimal Number:") #20.8
num2=input("Enter Second NonDesimal Number:") #10
print(float(num1)+float(num2)) #30.8

