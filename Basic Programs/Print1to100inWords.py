#  program to print 1 to 100 numbers in the words

mydict = {"0": "Zero ",
          "1": "One ",
          "2": "Two ",
          "3": "Three ",
          "4": "Four ",
          "5": "Five ",
          "6": "Six ",
          "7": "Seven ",
          "8": "Eight ",
          "9": "Nine "
          }

number = 420
word = ""

for ch in str(number):
    word += mydict[ch]


print(word)