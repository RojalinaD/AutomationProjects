# Merging 2 dictionaries

# Method-1 --> Using update()
"""
def merge_dicts(d1, d2):
    d3 = d1.update(d2)
    return d3


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}

print(merge_dicts(dict1, dict2))  # This returns None
print(dict1)  # This returns the updated dict1


# Method-2 --> Using '**'

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)


# Method-3--> Using '|' union operator

def merge_dicts(d1, d2):
    res = d1 | d2
    return res


# Driver code
dict1 = {'a': 11, 'b': 44}
dict2 = {'d': 66, 'c': 33}
dict3 = merge_dicts(dict1, dict2)

print(dict3) """


# Method-4 --> Using loop and .keys()

def merge_dicts(d1, d2):
    for i in d2.keys():
        d1[i] = d2[i]

    return d1


dict1 = {'a': 11, 'b': 44}
dict2 = {'d': 66, 'c': 33}
dict3 = merge_dicts(dict1, dict2)
print(dict3)
