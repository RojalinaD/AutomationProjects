# Check whether a string is Palindrome or not

old_str = input("Enter a string: ")
old_str = old_str.casefold()

new_str = ""

for char in old_str:
    new_str = char + new_str

if new_str == old_str:
    print("The string is palindrome")

else:
    print("The string is not palindrome")
