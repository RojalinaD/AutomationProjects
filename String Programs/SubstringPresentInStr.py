# Check if a substring is present in a str or not

# Method-1 --> Using if..in
"""
inp_str = input("Enter a string: ")
sub_str = "want"

if sub_str in inp_str:
    print("Yes,the substr {} is present in the str {}".format(sub_str,inp_str))

else:
    print("No, the substr is not present in the string")


# Method-2 --> Using split() and if..in

inp_str = input("Enter a string: ")
sub_str = "study"

split_str = inp_str.split()

if sub_str in split_str:
    print("yes")

else:
    print("no")

# Method-3 --> Using find() method
# find() returns -1 if a string is not found, otherwise it returns the index where the str was first found

def check_substr(inp,sub):

    if inp.find(sub) == -1:
        print("no")
    else:
        print("Yes,the substr was found at index {}".format(inp.find(sub)))



inp_str = input("Enter a string: ")
sub_str = "study"

check_substr(inp_str,sub_str)


# Method-4 --> Using count()

def check_str(inp,sub):

    if (inp.count(sub)) > 0:
        print("yes")

    else:
        print("no")


check_str("Rojalina", "al") """

# Method-5 --> Using index()
# index() returns the index of the position where the str was first found
# If the str was not found, then an error is thrown

inp_str = "Rojalina"
sub_str = "anil"

print(inp_str.index(sub_str))