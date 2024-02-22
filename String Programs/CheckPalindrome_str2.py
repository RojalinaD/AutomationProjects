# Check whether a string is palindrome or not

old_str = input("Enter a string: ")
old_str = old_str.casefold() # returns a lower case version of the original string

rev_str = old_str[::-1]
print(rev_str)

if rev_str == old_str:
    print("The string is Palindrome")

else:
    print("The string is not Palindrome")