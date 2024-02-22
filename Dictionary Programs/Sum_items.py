# Find the sum of all the items in a dictionary

# taking user input for a  dictionary
mydict = {}
count = 0
while count < 3:
    keys = input("Enter a key: ")
    mydict[keys] = int(input("Enter a value for the key: "))
    count += 1

print(mydict)

# Finding the sum of all the values of the dict
sum1 = 0 # when using the inbuilt method sum() in the same file never use another user defined
# variable of the same name,there will be errors

for values in mydict.values():
    sum1 += values

print(sum1)

# Using sum()

def dictsum(inpdict):
    return sum(inpdict.values())



dict1 = {"a": 100, "b": 200, "c": 300}
print(dictsum(dict1))

