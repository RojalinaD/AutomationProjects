# Lambda with filter()
# The filter() method filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_list = list(filter(lambda x: x % 2 == 0, list1))
print(filter_list)

print("****************************")

list2 = [1,2,3,4,5,6,7,8,9,10]
filter_list1 = list(filter(lambda x: x % 2, list1))
print(filter_list1)

# Lambda with map()
# You use the map() function whenever you want to modify every value in an iterable.

list3 = [1, 2, 3, 4, 5]
map_list = list(map(lambda x: pow(x, 2), list3))

# Lambda with List comprehension

is_even_list = map([lambda i:i*10 for i in range(1, 5)])

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item)
