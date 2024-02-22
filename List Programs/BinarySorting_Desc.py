# Binary Sort in Descending order without using a temp variable

list1 = [24, 56, 31, 98, 43, 72]

for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]


print(list1)