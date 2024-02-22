# Given two array A and B find array A is a subset of B or vice versa

# Method-1 --> Using a set

l1 = [3, 1, 5, 8, 6, 0, 2, 7]
l2 = [2, 13, 5, 7]

s1 = set()

for num1 in l1:
    s1.add(num1)

l_first = len(s1)

for num2 in l2:
    s1.add(num2)

l_second = len(s1)

if l_first == l_second:
    print("{} is a subset of {}".format(l2,l1))

else:
    print("{} is not a subset of {}".format(l2,l1))




