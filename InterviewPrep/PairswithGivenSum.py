
l1 = [2,6,1,9,4,3,7,5]
sum = 8

i = 0
j = i + 1
l2 = []
length = len(l1) - 1
while i < length:
    j = i + 1
    while j <= length:
        if l1[i] + l1[j] == sum:
            l2.append(l1[i])
            l2.append(l1[j])
            print(l2)
            j += 1

        else:
            j += 1

    i += 1
