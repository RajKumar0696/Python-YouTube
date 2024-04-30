Name = "Raj Kumar"
Age = 25
Company = "Nikki"
Salary = 20150.20

"""" integer=%d   string=%s   float=%g or %f"""
# -------------------------------------------------

# Approach 1
print(Name, Age, Company, Salary)

# Approach 2
print("name:", Name)
print("age:", Age)
print("company:", Company)
print("salary:", Salary)

# Approach 3 Using % operator  (using % (type) is important)
print("name:%s  age:%d  company:%s  salary:%f" % (Name, Age, Company, Salary))

print("name:%s" % (Name))
print("age:%d" % (Age))
print("company:%s" % (Company))
print("salary:%f" % (Salary))

# Approach 4 using {}  ( using {} value is importent)
print("name:{}  age:{}  company:{}  salary:{}".format(Name, Age, Company, Salary))

print("name:{}".format(Name))
print("age:{}".format(Age))
print("company:{}".format(Company))
print("salary:{}".format(Salary))

# Approch 5 (indox starting 0) (using {}type index and value both of importent)
print("name:{0}  age:{1}  company:{2}  salary:{3}".format(Name, Age, Company, Salary))
# This is valid in 0,0,0,0
print("name:{0}".format(Name))
print("age:{0}".format(Age))
print("company:{0}".format(Company))
print("salary:{0}".format(Salary))
