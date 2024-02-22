# Remove duplicate words from the string
# Method-1 --> Using set, doesn't maintain the order of words

str1 = "Hello Hello this is Java Java"
list1 = str1.split(" ")
print(list1)

"""
set1 = set(list1)

set2 = set()

for word in list1:
    set2.add(word)

print(set1)
print(set2)
"""

# Method-2 --> split a string and adding to a list. Removing duplicates from list. Order is maintained

i = 0

while i < len(list1):
    j = i + 1

    while j < len(list1):
        if list1[i] == list1[j]:
            list1.pop(j)
            j += 1

        else:
            j += 1

    i += 1





print(list1)






