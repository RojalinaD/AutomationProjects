# Basic Dict Methods
# Dictionaries are ordered,unindexed and mutable
# Note: Dictionary keys must be immutable, such as tuples, strings, integers, etc.
# We cannot use mutable (changeable) objects such as lists as keys.

# Declaring a dictionary
students = {}
capitals = dict()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# length of a dictionary
squares = {2: 4, 3: 9, 4: 16, 5: 25}
print(len(squares))
print("-----------------------------------------------------")


# Access dictionary items
rollnums = {1: "Ajeet", 2: "Sujeet", 3: "Ramesh", 4: "Suresh"}
print(rollnums[3])

print(squares.get(4))


# Change dictionary items
rollnums[1] = "Ajay"
print(rollnums)


# Add new items to the dictionary
# Using index
rollnums[5] = "Sanchita"

# Adding a new dict to the original dict
newrolls = {6: "Anil"}
rollnums.update(newrolls)
print(rollnums)

# Adding a tuple to the original dict

car.update([('color', 'white')])
print(car)

# delete all elements from a dictionary
car.clear()
print(car)
print("--------------------------------------")

# remove a single element from dict
# Using pop()
rollnums.pop(4) # removes by key
print(rollnums)

# Using del()
del rollnums[6] # deletes a particular key
print(rollnums)

# copy() of a dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cars = car.copy()
print(cars)

# fromkeys() method

 # keys for the dictionary
alphabets = {'a', 'b', 'c'} # keys can be any iterables like string, set, list, etc.

 # value for the dictionary
number = 1 # values can be of any type or any iterables like string, set, list, etc.
# Same value is assigned to all keys

 # creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)

print(dictionary)

# get() method

#The syntax of get() is:
"""
dict.get(key[, value])

get() method returns:

the value for the specified key if key is in the dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified. """

print(car.get("model"))

"""
Python get() method Vs dict[key] to Access Elements
get() method returns a default value if the key is missing.

However, if the key is not found when you use dict[key], KeyError exception is raised."""

# items() method

print(rollnums.items())  # returns a list of tuple pairs of keys and values

# keys() method

print(car.keys()) # returns a list of keys

# popitem() method

"""
The popitem() method removes and returns the (key, value) pair from the dictionary in the Last In, First Out (LIFO) order.

Returns the latest inserted element (key,value) pair from the dictionary.
Removes the returned element pair from the dictionary.
"""

result = rollnums.popitem()
print(result)

# Note: The popitem() method raises a KeyError error if the dictionary is empty.

# Loop through a dictionary


for keys in car: # by default looping through a dict returns keys
  print(keys)

print("--------------------------------------")
for keys in rollnums:
  print(rollnums[keys]) # prints values

print("------------------------------------------")

for val in car.values():
  print(val)

print("----------------------------------------------------")

for key,value in car.items():
  print(key, value)



