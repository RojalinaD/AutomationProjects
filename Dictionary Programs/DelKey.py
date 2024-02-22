# deleting a key from a dict using del and pop

dict1 = {1: "a", 2: "b", 3: "c"}

# del dict1[1]
print(dict1)

# dict1.pop(2)
# print(dict1)
# dict1.pop(2)

# using dict.items() and dict comprehension

new_dict = {key: val for key, val in dict1.items() if key != 2}
print(new_dict)
