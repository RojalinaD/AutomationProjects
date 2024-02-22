# SORT --> sort() is a method of list class and can only be used with lists.
# SORT returns nothing and makes changes to the original sequence.
# Syntax: List_name.sort(key)


# SORTED --> sorted() function sorts the given sequence as well as set and dictionary(which is not a sequence)
# either in ascending order(default) or in descending order
# Sorted() always returns a sorted list.
# This method doesn’t affect the original sequence.
# Syntax: sorted(iterable, key)


# Example - 1 --> Using sorted() function

L = [10, 3, 4, 2, 6, 1, 7, 8]

print("Sorted list:")
print(sorted(L))

print("\nReverse sorted list:")
print(sorted(L, reverse=True))

print("\nOriginal list after sorting:")
print(L) # sorted() function does not change the original list

print("-------------------------------------------")

# Example - 2 --> Demonstrate the use of sorted() with different types of iterables.Result is always a list

# List
l1 = ['q', 'w', 'r', 'e', 't', 'y']
print("\n", sorted(l1))

# Tuple
t1 = ('q', 'w', 'e', 'r', 't', 'y')
print("\n", sorted(t1))

# String-sorted based on ASCII translations
s1 = "python"
print("\n", sorted(s1))

# Dictionary
d1 = {'h': 1, 'c': 2, 'i': 3, 'o': 4, 'u': 5, 'l': 6}
print("\n", sorted(d1)) # By default, sorted() will sort a dict based on the keys

# Set
set1 = {'q', 'w', 'e', 'r', 't', 'y'}
print("\n", sorted(set1))

print("-------------------------------------------")

# Sorted() with key parameter

L = ['aaaa', 'bbb', 'cc', 'd']

# sorted without key parameter
print(sorted(L))
print()

# sorted with key parameter
print(sorted(L, key=len))

# Example - 3 --> Demonstrate use of sort() method

numbers = [1, 3, 4, 2]

# Sorting list of Integers
numbers.sort()

print(numbers)

words = ["Geeks", "For", "Geeks"]

# Sorting list of strings
words.sort()

print(words)

# List of Integers
numbers = [1, 3, 4, 2]

# Sorting list of Integers in reverse
numbers.sort(reverse=True)

print(numbers)


# function to return the second element of the
# two elements passed as the parameter


def sortSecond(val):
    return val[1]


# list1 to demonstrate the use of sorting
# using  second key
list1 = [(1, 2), (3, 3), (1, 1)]

# sorts the array in ascending according to
# second element
list1.sort(key=sortSecond)
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)