# Check if a string is Palindrome or not using a function

def ispalindrome(inpstr):

    revstr = ''.join(reversed(inpstr))

    if inpstr == revstr:
        return True
    else:
        return False



oldstr = input("Enter a string: ")
print(ispalindrome(oldstr))