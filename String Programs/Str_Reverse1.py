# reversing a string ---- 1

str1 = "I am learning Python"
l1 = str1.split() # split() method always returns a list
print(l1)

i = len(l1) - 1
l2 = []

while i >= 0:
    l2.append(l1[i])
    #str2 = " ".join(l1[i]) # join() method converts a list (with contents as strings) to strings
    i -= 1

print(" ".join(l2))