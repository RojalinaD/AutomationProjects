num = int(input("Enter a number: "))
result = 1

while num >= 1:
    result = num * result
    num = num - 1

print(result)