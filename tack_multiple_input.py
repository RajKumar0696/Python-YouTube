# Give two values in one time
# if you give the input like tish 10 20 (only give space)

a, b = input("Enter two values:").split()
print("Number no is :", a)
print("Number two is:", b)

# Multiple value in single time

a, b, c, d, e = input("Enter multiple value:").split()
print("one:", a, "\n" "two:", b, "\n" "three:", c, "\n" "four:", d, "\n" "five:", e, "\n")

x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()
