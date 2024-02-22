# Rotate an array to right by K no. of times

list1 = [3, 8, 9, 7, 6]
k = 0

while k < 2:

    j = len(list1) - 1
    temp = list1[j]
    while j > 0:
        i = j - 1
        list1[j] = list1[i]
        j -= 1

    list1[i] = temp
    k += 1

print(list1)
