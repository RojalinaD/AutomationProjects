# Return array of indices that sum to given number K

l1 = [1, 3, 5, 7, 10, 4]
k = 10
#l1.sort()
print(l1)

i = 0
j = len(l1) - 1

l2 = []

while i < j:

    if l1[i] + l1[j] < k:

        i += 1

    elif l1[i] + l1[j] > k:

        j -= 1

    else:

        l2.append(i)
        l2.append(j)
        i += 1
        j -= 1



print(l2)