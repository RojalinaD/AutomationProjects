# check if 2 strs are anagrams
# Method - 1
"""
from collections import Counter

str1 = "Listenn"
str2 = "Silent"

str1 = str1.casefold()
str2 = str2.casefold()

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")

# Method-2

s3 = "dad"
s4 = "add"

def checkanagrams(str3,str4) :

    if Counter(s3) == Counter(s4):
        print("------------------")
        print("Anagrams")
    else:
        print("Not Anagrams")


checkanagrams(s3,s4)

# Method - 3

s1 = "listen"
s2 = "silent"

l1 = [s1[i] for i in range(len(s1))]
l2 = [s2[j] for j in range(len(s2))]

if l1.sort() == l2.sort():
    print("-------------------")
    print("Anagrams")
else:

    print("Not Anagrams")

"""

# Method 4

def checkanagrams (str1,str2):

    if len(str1) != len(str2):
        return False

    counts = {}

    for c1,c2 in zip(str1,str2):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1

        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = 1


    for val in counts.values():
        if val != 0:
            return False
        return True


s1 = "listen"
s2 = "silent"

if checkanagrams(s1,s2):
    print("Anagrams")

else:
    print("Not Anagrams")

