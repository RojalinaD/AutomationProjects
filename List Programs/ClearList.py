# Clear a list using clear() method

count = 1
list1 = []

while count < 7:
    list1.append(int(input("Enter the values: ")))
    count += 1

print(list1)

#list1.clear() # clear() method clears the contents of the list
#print(list1)

#del(list1) # del() method deletes the entire list
#print(list1)


while len(list1) > 0:
    list1.pop()  # pop() method pops out the last index from the list

print(list1)

