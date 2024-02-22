# Count chars in str
str1 = "programming"
dict1 = {}

for char in str1:
    if char not in dict1:
        dict1[char] = 1

    else:
        dict1[char] += 1


print(dict1)

