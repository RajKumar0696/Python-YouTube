# Case 1
a = 31
if a > 30:
    print("True Condition")
else:
    print("False Condition")

# Case 2
if False:
    print("True condition")
else:
    print("False Condition")

# Case 3
if 0:
    print("True Condition")
else:
    print("Flase Condition")

# Case 4  Even or Add Number
a = 6
if a % 3 == 0:
    print("True Condition")
else:
    print("False Condition")

# Multiple statments if block
if False:
    print("Statment 1")
    print("Statment 2")
    print("Statment 3")
    print("Statment 4")
    print("Statment 5")
else:
    print("Statment 6")
    print("Statment 7")
    print("Statment 8")
print("I am Rajkumar")  # sperate statement not part of else block

# Single Statment in Single line

print("Ture Condition") if True else print("Flase Condition")
print("Ture Condition") if False else print("Flase Condition")
print("Welcome") if True else print("Python")
print("Welcome") if False else print("Python")
print("Welcome") if 10 > 20 else print("Python")
print("Welcome") if 10 < 20 else print("Python")

# Multiple Statment in sigle line

# {print("Welcome Raj"),print("Python Raj")} if True else {print("Not Welcome Raj"),print("Not Python Raj")}
# {print("Welcome Raj"),print("Python Raj")} if False else {print("Not Welcome Raj"),print("Not Python Raj")}

#
# (print("Welcome Raj"),print("Python Raj")) if False else (print("Not Welcome Raj"),print("Not Python Raj"))
# (print("Welcome Raj"),print("Python Raj")) if True else (print("Not Welcome Raj"),print("Not Python Raj"))


""" Conditional Statment elif"""

a = 5
if a == 10:
    print("TEN")
elif a == 20:
    print("TWENTY")
elif a == 30:
    print("THIRTY")
elif a == 35:
    print("THIRTY FIVE")
else:  # NOT MANDOTRY(oru velai eles tharalanalum statment run agum)
    print("NOT MATCHES IN LIST")
