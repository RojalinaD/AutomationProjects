# Reversing a string ----- 2

str1 = " I am learning Python Programming"

str2 = str1.split()[::-1]
print(str2)

l1 = []
for i in str2:
    l1.append(i)


print(" ".join(l1))


