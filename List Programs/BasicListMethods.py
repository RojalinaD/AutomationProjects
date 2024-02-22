# Basic List Methods
# Lists are ordered,indexed,iterable and mutable

# Declaring an empty list
nums = []
names = list()

# length of a list -- len()
numbers = [5, 8, 1, 9, 3, 0]
print(len(numbers))
print("------------------------------------------")

# Looping through a list
# Using for loop
mylist = ["apple", "banana", "cherry"]
for fruits in mylist:
    print(fruits)

# For loop using index and range
i = 0
j = 0
for i in range(len(mylist)):
    print(mylist[i])

# Using while loop
while j < len(mylist):
    print(mylist[j])
    j += 1

print("-----------------------------------------------")


# append()
l1 = [1, 2, 3, 5, 7, 9, 0]
l1.append(10)
print(l1)

l1.append("Rose")
print(l1)

# extend()
l2 = [11, 12, 14]
l1.extend(l2)
print(l1)

# insert()
l1.insert(2, 'Lily')  # takes index where ele has to be inserted and the ele to be inserted
print(l1)

# sort()
l2 = [21, 43, 12, 65, 98, 76]
l2.sort()
print(l2)

str1 = ["Apple", "Orange", "Peach", "Mango"]
str1.sort()  # Sorts alphabetically
print(str1)
print("-------------------")

# reverse() # reverses the list in place and returns the changed list
l2.reverse()
str1.reverse()
l1.reverse()
print(l1)
print(l2)
print(str1)
print("-------------------")

# pop() # removes the index specified
str1.pop(0)
print(str1)

# clear() # clears the list
l1.clear()
print(l1)

# remove() # removes the first occurrence of the element
str1.insert(3, 'Orange')
str1.remove("Orange")
print(str1)
print("-------------------")

# index() # returns the index of the first occurrence of the element
print(str1.index("Apple"))

# print(str1.index("Peach")) # returns an error bcz 'Peach' is not in the list

# copy() # returns a copy of the list
print(l2.copy())

# count() # returns count of the specified element
str1.insert(0, "Peach")
str1.insert(1, 'Orange')
print(str1)
print(str1.count("Orange"))

# length of a list -- len()
print(len(str1))
