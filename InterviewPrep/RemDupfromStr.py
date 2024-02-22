
# Remove duplicates from string
# Method - 1

str = "Hellooo"

set1 = {x for x in str} # Set comprehension

set2 = set(str)

print(set1)
print(set2)

# Method - 2

str1 = "Words to split"
l1 = list(str1)
print(l1)




i = 0
j = i + 1

while (i < len(l1) - 1):
    j = i + 1
    while j < len(l1):

        if l1[j] == l1[i]:
            l1.remove(l1[j])
            j += 1

        else:
            j += 1

    i += 1

print(l1)

str2 = "".join(l1)
print(str2)
