# Make a new string using the first 2 chars and last 2 chars from an input string
# If string length is less than 2, return "Empty String"

def newstring(str):

    if len(str) < 2:

        print("Empty String")

    else:

        newstr = str[0:2] + str[-2:]

        return newstr

inpstr = input("Enter a string: ")
print(newstring(inpstr))