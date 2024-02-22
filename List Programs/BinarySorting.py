# Sort an array/list using Binary Sorting technique

list1 = [2, 6, 1, 8, 6, 5, 0, 12, 65, 34]
i = 0
j = i + 1
temp = 0
size = len(list1) - 1

while size > 0:
    i = 0
    j = i + 1
    while j <= size:
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
            i += 1
            j += 1

        else:
            i += 1
            j += 1

    size -= 1



print(list1)