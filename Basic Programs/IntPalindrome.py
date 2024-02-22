# Check if an int is palindrome or not

# Method - 1 --> Convert int to str and check with the reverse of the str

num = 5335
var = str(num) == str(num)[::-1]  # Returns True/False

print(var)

# Method - 2 --> Take the user input as string

str1 = input("Enter a num: ")
print(str1 == str1[::-1])

# Method - 3 --> Using while loop

num1 = int(input("Enter a number: "))

temp = num1
rev_num = 0

while num1 > 0:  # num1 = 535
    dig = num1 % 10  # 56 % 10 = 6
    rev_num = rev_num * 10 + dig  # 0 * 10 + 6 = 6
    num1 = num1 // 10


if rev_num == temp:
    print("Palindrome")
else:
    print("not palindrome")


