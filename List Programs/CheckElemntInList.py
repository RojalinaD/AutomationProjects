# Check if an element exists in list
# Using naive method
from collections import Counter

list1 = ["apples", "bananas", "oranges", "pears"]

if "peaches" in list1:
    print("yes")

else:
    print("no")

# checking if an element exists by using a loop

for fruits in list1:
    if fruits == "oranges":
        print("exists")
    else:
        print("not exists")

# Using list inbuilt  count method

list2 = ["apples", "bananas", "oranges", "pears"]

ele_cnt = list2.count("pears")

if ele_cnt > 0:
    print("Element exists")
else:
    print("Element does not exist")


# Using find() and map() method in case the list contains only numbers

numbers = [10, 20, 30, 40, 50, 60, 70]

# The map function can be used in 2 cases to convert a list to a string.
  #if the list contains only numbers.
  #If the list is heterogeneous

num_str = list(map(str, numbers)) # map() takes 2 args- str func and the iterative.This step returns a list of strings
print(num_str)

num_str2 = " ".join(map(str, num_str)) # this step returns a string separated by space
print(num_str2)

if num_str2.find("40") != -1: # find() method helps to find a substring inside a string.
# #find() Returns -1 if string is not found
   print("element is present in the list")

else:
    print("element is not present in the list")

# Using Counter from Collections

newlist = Counter(list1)

if newlist["apples"] > 0:
    print("Element exists")

else:
    print("Element doesn't exist")
