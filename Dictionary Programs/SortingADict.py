# Dictionaries are unordered.They maintain the insertion order
# Dictionaries can't be ordered in place
# Even though they preserve insertion order they are not called a sequence bcz
# dict are sets of key-value pairs and the sets are  unordered
# We can't move around the key-val pairs and insert at a particular index

# Example-1

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(people.items()) # The items() method returns a view object that
# displays a list of dictionary's (key, value) tuple pairs.

# Sort by key
print(sorted(people.items())) # Here sorted() will sort the list of tuples based on the dict keys


# Sort by value
print(sorted(people.items(), key=lambda item: item[1]))

# Passing a dict directly to sorted() will return a sorted list of dict keys only
# If you want to conserve all the information from a dictionary when sorting it,
# the typical first step is to call the .items() method on the dictionary.
# Calling .items() on the dictionary will provide an iterable of tuples representing the key-value pairs:








