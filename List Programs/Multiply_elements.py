# Multiply all elements of a list

list_num = [2,4,5,1,6]
prod = 1

for num in list_num:
    prod = prod*num

print("The product of all numbers in the list is {}".format(prod))

# Using recursion

def recur_multi(inp_list):
    if len(inp_list) < 1:
        return 1
    else:
        return inp_list[0]*recur_multi(inp_list[1:])



l1 = []
print(recur_multi(l1))