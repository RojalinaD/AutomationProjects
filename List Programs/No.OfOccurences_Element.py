# Count no. of occurrences of an element
from collections import Counter

# Method-1 --> Using loop

lst = [2, 4, 1, 5, 1, 6, 2, 4, 1]
num = 1
count = 0

for numbers in lst:
    if numbers == num:
        count += 1


print(count)

# Method-2 --> Using count()

alphabets = ['a', 'c', 'd', 'a', 'a', 'b', 'e']

def count_ele(lst, ele):
    return lst.count(ele) # count returns the no. of times an element occurs.
    # If the ele is not found at all, it returns 0


print(count_ele(alphabets, 'z'))

# Method-3 --> Using Counter(). Has to imported from Collections
# Counter returns a dict with elements and their occurrences as key:value pairs

num = 1
nums_dict = Counter(lst)
print("The element {} occurs {} times".format(num, nums_dict[num]))

letter = 'b'
alpha_dict = Counter(letter)
print("The element {} occurs {} times".format(letter, alpha_dict[letter]))

# Method-4 --> using Dictionary Comprehension


alpha_dict = {item: alphabets.count(item) for item in alphabets}
print("The no. of times {} occurs is {}".format(letter, alpha_dict[letter]))
