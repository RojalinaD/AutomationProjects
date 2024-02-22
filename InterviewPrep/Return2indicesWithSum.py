#	return array with index of first matching pair with given sum
#   Eg: int[] arr= {3, 5, 7, 3, 4, 9} sum = 10 output= [0,2]

l1 = [2,1,4,5,6,3,9,8]

op_list = []

sum = 11

i = 0
j = i + 1

len = len(l1) - 1


while i < len:

    while j <= len:

        if l1[i] + l1[j] == sum:
            op_list.append(i)
            op_list.append(j)
            break

        else:
            j += 1

    i += 1


print(op_list)

