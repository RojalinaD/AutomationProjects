# Learning List Comprehension

# List Comprehension is a precise and elegant way of creating lists

# Example - 1 --> without a conditional statement
words = ["data", "science", "machine", "learning"]

list_words = [len(i) for i in words]
print(list_words)

# Example - 2 --> with a conditional statement
list_words1 = [len(i) for i in words if len(i) > 5]
print(list_words1)

# Example - 3 --> with enumerate statement
list_names = ['Tim', 'Ron', 'Andy', 'Keith']
tup_names = list(enumerate(list_names, start=1))
print(tup_names)




