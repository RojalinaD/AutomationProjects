l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    print(i)
    print("---------------------------")
    for j in range(i + 1, len(l1)):


        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

        print(l1)

# sorted list
print("Sorted List", l1)
