# Split even and odd elements into 2 lists

# Method - 1

inp_list = [24,13,35,42,65,76,86,36,43,77,89]

evennums = [num for num in inp_list if num % 2 == 0]
oddnums = [num for num in inp_list if num % 2 != 0]

print("list of even numbers = ", evennums)
print("list of odd numbers = ", oddnums)

# Method - 2

l1 = []
l2 = []

for nums in inp_list:
    if nums % 2 == 0:
        l1.append(nums)

    else:
        l2.append(nums)

print(l1,l2)