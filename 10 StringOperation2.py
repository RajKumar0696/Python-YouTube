# # in and not in operations
# str=("Rajkumar")
# print("kumar" in str) #true
# print("Raj" in str)# true
# print("abc" in str)# flase
#
# print("Raj" not in str) #false
# print("raj" not in str)# true
#
#
# #Comparison operation  (<,>,<=,>=,!=,==)
#
# print("Raj"=="raj") # false
# print("Raj"=="Raj") # true
# print(("yellow"<"hello")) # false ( y is bigger and h is smaller ) value consider in ASCII
# print(("yellow">"hello")) # true
# print("Arrow"<="Arow")# false
# print("Arrow">="Arow") #true
# print("Raj"!="Mithansh") # true
# print("Raj"!="Raj") # false

# iterating string using for loop
#
# str=("Rajkumar")
# for i in str:
#     print(str)

str=("Rajkumar")
for i in str:
    print(i)

print(str, end="\n")
print(str, end="")
print(str, end="foo")


# #Testing Strings *** consider in whitespace in testing
#
# s=("welcome")
# print(s.isalnum()) #true
# print(s.isalpha()) #True
# print(s.isdigit()) #False
# print(s.isidentifier()) #true
# print(s.islower())#true
# print(s.isupper()) #False
# print(s.isspace()) #False
#
#
#
#
# #Searching for substings
#
# s=("welcome of python")
# print(s.endswith("come")) # false
# print(s.endswith("thon")) # true
# print(s.startswith("wel")) #true
# print(s.startswith("thon")) #false
# print(s.count("o")) #3
# print(s.count("y")) #1
# print(s.count("of")) #1
# print(s.find("h")) #14
# print(s.find("o")) #4 just use find return value is startin o place value
# print(s.rfind("o")) # 15 use rfind return last o place value
#
#
#
# #Converting stings
#
# s=("welcome to PYTHON rajkumar ")
# print(s.capitalize())#Welcome to python rajkumar
# print(s.lower()) # welcome to python rajkumar
# print(s.upper()) #WELCOME TO PYTHON RAJKUMAR
# print(s.title())#Welcome To Python Rajkumar
# print(s.swapcase()) #WELCOME TO python RAJKUMAR
# print(s.replace("to","of")) #welcome of PYTHON rajkumar
#
