# Reversing a string using all methods

# Method - 1 --> Using split and join

inpstr = "I am learning python"
inp_list = inpstr.split()

i = len(inp_list) - 1
newlist = []

while i >= 0:
     newlist.append(inp_list[i])
     i -= 1

newstr = " ".join(newlist)

print(newstr)

# Method - 2 --> Using reversed()
# reversed() method computes the reverse of a given sequence object(tuples,str,list)
# and returns it in the form of a list.

inp_str = "I am learning Java"
inp_list1 = inp_str.split()
new_list2 = reversed(inp_list1)
new_str1 = " ".join(new_list2)
print(new_str1)

# Method - 3 --> Using normal loop method and traversing from end

inp_str1 = "Umbrella"
new_str2 = ""


for char in inp_str1:
     new_str2 = char + new_str2


print(new_str2)



