# Reverse a list in place

list1 = [10, 20, 30, 40, 50, 60]

temp_var = 0
i = 0
j = len(list1)-1

while i < j:
    temp_var = list1[i]
    list1[i] = list1[j]
    list1[j] = temp_var
    i += 1
    j -= 1

print(list1)

# Reverse a list using reverse() method

list1.reverse() # reverse() is a method
print(list1)

# Reverse a list using slicing method

rev_list = list()

rev_list = list1[::-1]
print(rev_list)

# Reverse a list using reversed function

list2 = ["Apples", "Oranges", "Bananas", "Peaches"]
for fruits in reversed(list2): # reversed() is a function that takes only strings
    print(fruits)
