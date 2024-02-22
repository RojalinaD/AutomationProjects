# Merging 2 lists

# Method - 1
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
#l1.extend(l2)
#print(l1)

# Method - 2
l3 = l1 + l2
print(l3)

# Method - 3
l4 = []

for num1 in l1:
    l4.append(num1)

for num2 in l2:
    l4.append(num2)

print(l4)