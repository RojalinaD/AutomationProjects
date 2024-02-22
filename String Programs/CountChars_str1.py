# Count how many times each char occurs in a string

char_dict = {}

inp_str = input("Enter a string: ")

for char in inp_str:
    if char in char_dict:
        char_dict[char] += 1

    else:
        char_dict[char] = 1

 
print(char_dict)
