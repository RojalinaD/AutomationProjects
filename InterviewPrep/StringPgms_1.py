# reverse a str

str1 = "I love Python"
list1 = str1.split(' ')
print(list1)

str2 = ""
"""
i = len(list1) - 1
while i >= 0:
    str2 = str2 + list1[i] + " "
    i -= 1


str2 = str1[::-1]



str2 = "".join(reversed(str1))
"""

str2 = ""

for ch in str1:
    str2 = ch + str2

print(str2)

