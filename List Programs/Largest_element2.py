# find the largest element in a list using normal loop

count = 1
list1 = []

while count <= 6:
    list1.append(int(input("Enter a num: ")))
    count += 1

print(list1)
max = list1[0]

for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]

  #  else:
   #     continue

print("The largest of all elements is {}". format(max))

# find the largest element using inbuilt max() method

list1 = [23, 42, 13, 65, 10, 3]
print(max(list1))