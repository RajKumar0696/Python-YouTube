# create a dictionary
family = {"Raj": "11-22-33", "Hema": "44-55-66"}
print(family)  # {'Raj': '11-22-33', 'Hema': '44-55-66'}

# retrieving
print(family["Raj"])  # 11-22-33

# Adding
family["mithansh"] = "77-88-99"
print(family)  # {'Raj': '11-22-33', 'Hema': '44-55-66', 'mithansh': '77-88-99'}

# Modified
family["mithansh"] = "77-88-789"
print(family)  # {'Raj': '11-22-33', 'Hema': '44-55-66', 'mithansh': '77-88-789'}

# Delete
del (family["mithansh"])
print(family)  # {'Raj': '11-22-33', 'Hema': '44-55-66'}

# Looping items in the dictionary
# Just reading for loop
friends = {'a': '100',
           'b': '200',
           'c': '300',
           'd': '400'
           }
for x in friends:
    print(x, ":", friends[x])

# find the lenght of dictionary
print(len(friends))  # 4

# equality testing in dictionary (== and !=) only use
d1 = {"Raj": "11", "Kumar": "22"}
d2 = {"kumar": "22", "Raj": "11"}
print(d1 == d2)  # False
print(d1 != d2)  # True

# Dictionary items
# popitem()  randomly select the element show and delete
family = {'Raj': '11-22-33', 'Hema': '44-55-66', 'mithansh': '77-88-99'}
print(family.popitem())
print(family)

# clear (clear the dictionary)
print(family.clear())  # None

# Keys (return the keys in dictionary)
family = {'Raj': '11-22-33', 'Hema': '44-55-66', 'mithansh': '77-88-99'}

print(family.keys())  # dict_keys(['Raj', 'Hema', 'mithansh'])

# values
print(family.values())  # dict_values(['11-22-33', '44-55-66', '77-88-99'])

# get (key) you enter the key name print the key value
print(family.get("Raj"))  # 11-22-33
print(family.get("Hanisha"))  # None

# pop(key) you enter the key name print the value and delete in the dictionary
print(family.pop("Raj"))  # 11-22-33
print(family)  # {'Hema': '44-55-66', 'mithansh': '77-88-99'}


