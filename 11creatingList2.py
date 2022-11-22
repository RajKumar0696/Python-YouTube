# #appand
list1=[1,4,6,8,90,7]
list1.append(16)
print(list1)
#extended
list2=[19,18]
list1.extend(list2)
print(list1)
#index
print(list1.index(90))
print(list1) #[1, 4, 6, 8, 90, 7, 16, 19, 18]
#pop
print(list1.pop(3))
print(list1)
#count
print(list1.count(6))
#insert
list1.insert(4,20)
print(list1)
#remove
list1.remove(90)
print(list1)
#reverse
list1.reverse()
print(list1)
#sort
list1.sort()
print(list1)

### List Comprehension

list1=[x for x in range(10)]
print(list1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list1=[x+1 for x in range(10) ]
print(list1)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list1=[x for x in range(10) if x % 2==0]
print(list1) #[0, 2, 4, 6, 8]

list1=[x for x in range(10) if x%3==0]
print(list1)

