# Find the largest element in an list using sort()

list1 = []
count = 1

while count <= 10:
    list1.append(int(input("Enter a num: ")))
    count += 1

print(list1)
list1.sort() # sort function sorts the list in an ascending order

print(list1)
