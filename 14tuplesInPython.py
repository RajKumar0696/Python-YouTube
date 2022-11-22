# #Tuples in python
t1=()
t2=(11,22,34,44,55)
t3=tuple("122433513")
t4=tuple("RAJKUMAR")
print(t1) #empty tuple file creaded
print(t2)# (11, 22, 34, 44, 55)
print(t3) #('1', '2', '2', '4', '3', '3', '5', '1', '3')
print(t4) #('R', 'A', 'J', 'K', 'U', 'M', 'A', 'R')


# Tuple Functions
t1=(23,324,56,78,54,34,6776,4523,34,34,7,54)
print(min(t1)) #7
print(max(t1)) #6776
print(len(t1)) #12
print(sum(t1)) #11997

#Iterating through Tupls

t1=(23,324,56,78,54,34,6776,4523,34,34,7,54)
for i in t1:
    print(i,end="")

#Slicing Tuples
t1=(23,324,56,78,54,34,6776,4523,34,34,7,54)
print(t1[4:6])
print(t1[0:4])
print(t1[:8])

#in and not in operators

t1=(23,324,56,78,54,34,6776,4523,34,34,7,54)
print(56 in t1)
print(44 in t1)
print(34 not in t1)
print(65 not in t1)

