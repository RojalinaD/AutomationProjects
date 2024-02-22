# Remove ith character from string

# Method - 1 --> Using normal method by looping

inp_str = "Geeeks for Geeks"
new_str = ""

for i in range(len(inp_str)):
    if i != 2:
        new_str = new_str + inp_str[i]


print(new_str)

# Method - 2 --> Using str.replace()

# str.replace() with index
inp_str1 = "Geeeks for Peeks"
new_str1 = inp_str1.replace('e', '', 1) # Providing index is necessary when there are duplicate elements

print(new_str1)

# str.replace() without index
inp_str2 = "Geeeks for Meeks"
new_str2 = inp_str1.replace('e', '') # Without index all duplicate elements are replaced
print(new_str2)


# Method - 3 --> Using slice and concatenation
inp_str3 = "This a is PyCharm"
new_str3 = inp_str3[:5] + inp_str3[7:] # Leaving out 'a' and ' '
print(new_str3)

# Method - 4 --> Using join() and list comprehension

inp_str4 = "I am an learning Python"
new_str4 = ''.join([inp_str4[i] for i in range(len(inp_str4)) if i != 5 and i != 6]) # removing 'an' from the string
# and joining the resulted list to make a new string bcz list comprehension returns a list

print(new_str4)


