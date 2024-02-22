# Find length of a list
from collections import Counter

list1 = [10, 20, 30, 40, 50, 60]
print(len(list1))

# finding length of a list using a counter

count = 0

for num in list1:
    count += 1

print(count)

# finding length of a list using sum() function
list2 = [2, 6, 1, 8, 9, 3, 5, 7]

list_len = sum(1 for num in list2)

print(list_len)

# finding length of a list using Collections Counter

list_len = sum(Counter(list2).values())
# A Counter is a subclass of dict. Its a container included in Collections module
# Therefore it is an unordered collection where elements and their respective count are stored as a dictionary.
# In the above example Counter(list2) returns a dict. The keys are the elements and their values are the count of
# the elements. So Counter(list2).values() returns the count of all elements. Sum() returns the sum of all the values

print(list_len)

