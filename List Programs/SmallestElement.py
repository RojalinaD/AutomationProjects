# Find the smallest number in the list

# Using traversal
numbers = [2,6,2,8,5,9,4]

min_nums = numbers[0]

for num in numbers:
    if num < min_nums:
        min_nums = num


print("The smallest number in the list is {}".format(min_nums))

# Using inbuilt function min()

l2 = [10,8,12,0,23,67]
print(min(l2))

# Sorting in an ascending order

l3 = [35,89,12,42,24]
l3.sort()
print(l3[0])