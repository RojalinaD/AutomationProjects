# To find the sum of all elements in an array
from operator import add

count = 5
list1 = []

while count >= 1:
    list1.append(int(input("Enter a number: ")))
    count -= 1

print(list1)

sum2 = 0

for num in list1:
    sum2 = num + sum2

print("The sum of all the elements is {}".format(sum2))

# Finding sum of all elements using enumerate() function

list3 = [2, 4, 6, 7, 8, 9, 1]

sum1 = 0

for i, ele in enumerate(list3):
    sum1 += ele

print(sum1)
print("--------------------")

# using sum() function

total = sum(list3) # sum() takes 2 parameters,(iterable,start).It adds the sum of the elements in iterable to the start.
# The start is 0 by default
total1 = sum(list3, 10)
print(total1)
print("--------------------")
print(total)

# using add() function

list4 = [2, 4, 6, 8, 10, 12]
result = 0

for i in list4:
    result = add(i, result) # add() adds each element in the iterable and returns the result
print("------------------")
print(result)
print("-------------------")

# Using list comprehension
list4 = [3, 6, 9, 12, 15, 21]
res = [i for i in list4]
print(sum(res))



