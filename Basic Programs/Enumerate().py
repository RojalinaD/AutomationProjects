# To illustrate the enumerate() function

# enumerate() function adds a counter to the iterable and returns it.The returned object is an enumerate object
# We can convert enumerate() objects
# enumerate() syntax is (iterable, start=0).If start is omitted, then by default it starts from 0

languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))
print("-------------------")

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# You can convert enumerate objects to list and tuple using list() and tuple() functions respectively.

grocery = ['bread', 'milk', 'butter']
enumerate_grocery = enumerate(grocery)

print(type(enumerate(grocery))) # <class 'enumerate'>
print("-------------------")

# converting to list
print(list(enumerate_grocery))
print("-------------------")

# changing the default counter
enumerate_grocery = enumerate(grocery, 10)
print(enumerate_grocery)
print("-------------------")
#print(list(enumerate_grocery))
print(tuple(enumerate_grocery)) # returns a tuple of tuples
print("-------------------")

# Looping through an Enumerate object

for item in enumerate(grocery):
    print(item)

print("-------------------")

for count, item in enumerate(grocery):
    print(count, item)
print("-------------------")

for count, item in enumerate(grocery, start=10):
    print(count, item)

