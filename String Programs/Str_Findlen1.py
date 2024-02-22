# Find the length of a string

count = 0

str1 = input("Enter a string: ")

#for i in range(len(str1)):
 #   count += 1

for char in str1:
    count += 1


print("The length of the string is: {}".format(count))