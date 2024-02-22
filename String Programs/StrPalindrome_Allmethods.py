# Check if a str is palindrome or not

# Method - 1 --> Split a str into a list and then reverse the list and join back

str1 = "Hello this is Java"
list1 = str1.split(" ")

list1.reverse()
print(list1)

str2 = ""
j = len(list1) - 1

str2 = " ".join(list1)
print(str2)

# Method - 2 --> extract a string from the end

str3 = "My name is Rojalina"
nstr = str3[::-1]

print(nstr)

# Method - 3 --> Using reversed()

str4 = "My name is Sanchita"
nstr1 = "".join(list(reversed(str4)))  # reversed takes an indexable object (no set/dictionary)

print(nstr1)
