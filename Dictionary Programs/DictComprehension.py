# Learning Dict Comprehension

# Dictionary comprehension is an elegant way of creating dictionaries
# Example-1 --> without a conditional statement

words = ["data", "science", "machine", "learning"]

dict_words = {i:len(i) for i in words}
print(dict_words)

# Example-2 --> with a conditional statement

dict_words1 = {i:len(i) for i in words if len(i) > 5}
print(dict_words1)

# Example - 3 --> more complicated conditional statement

dict_words2 = {i:len(i) if len(i) > 5 else 'short' for i in words}
print(dict_words2)

# Example - 4 --> dict comprehension by iterating over 2 iterables

values = [5, 2, 4, 7]
dict_values = {i:j for i, j in zip(words, values)}
print(dict_values)

# Example - 5 --> iterating over 2 iterables using if condition

dict_values1 = {i: j for i, j in zip(words, values) if j > 2}
print(dict_values1)

# Example - 6 --> Using enumerate with dict comprehension

names = ['Tim', 'Ron', 'Andy', 'Keith']
dict_names = {i: j for i, j in enumerate(names)}
print(dict_names)
