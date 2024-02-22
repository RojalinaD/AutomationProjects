# Reversing a string ----- 3

def rev_string(inpstring):

    words = inpstring.split(" ")
    print(words)
    rev_words = " ".join(reversed(words))
    return rev_words


str1 = "I am learning Python"
print(rev_string(str1))


