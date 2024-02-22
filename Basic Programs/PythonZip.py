# Learning Zip in Python

# Python Zip() function takes 2 iterables and aggregates them in a tuple and returns it
# Example - 1

languages = ["Python", "Java", "C"]
versions = [4, 3, 2]

results = zip(languages, versions)
#print(list(results)) # zip object returned can be converted into a list or dict or a set
# by using list() or dict() or set()
print(dict(results))

# If we do not pass any parameter, zip() returns an empty iterator
# If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
# If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements
# from all the iterables.Suppose, two iterables are passed to zip(); one iterable containing three
# and other containing five elements.Then, the returned iterator will contain three tuples.
# It's because the iterator stops when the shortest iterable is exhausted.

# Example - 2
# Passing diff. num of iterable elements
numbers_list = [1, 2, 3]
numbers_str = ["one", "two", "three"]
numbers_tuple = ("ONE", "TWO", "THREE")

results_list = zip() # with 0 parameters
print(list(results_list))

results_set = zip(numbers_list) # with 1 parameter
print(set(results_set))

results_dict = zip(numbers_list, numbers_str) # with 2 parameters
print(dict(results_dict))

results_tuple = tuple(zip(numbers_list, numbers_str, numbers_tuple))
print(results_tuple)

# Unzip()
list1, str1, tup1 = zip(*results_tuple) # unzip
print(list1, str1, tup1)