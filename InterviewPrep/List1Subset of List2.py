# Check if a list is subset of another list
# Method - 1

"""
list1 = [3,1,6,9,2,0,4,7,8,4]
list2 = [7,3,7]

set1 = set(list1)
set2 = set(list2)

if set2.issubset(set1):
    print("{} is a subset of {}".format(list2, list1))

else:
    print("{} is not a subset of {}".format(list2, list1))


# Method - 2

list3 = [3,9,1,6,4,2,4,0,3,1,8,8]
list4 = [3,1,8,3,2]

set3 = set(list3)
set4 = set(list4)

if set3 & set4 == set4:
    print("{} is a subset of {}".format(list4, list3))
"""

# Method - 3

l1 = [2,5,1,8,0,3,6,7]
l2 = [4,1]

flag = 0
result = set(num in l1 for num in l2)

for res in result:
   if res == False:
     flag = 1


if flag == 1:
    print("not subsets")
else:
    print("subsets")

