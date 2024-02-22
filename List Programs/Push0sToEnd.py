# Move all zeros to end of the array

numbers = [2, 0, 4, 6, 8, 0, 1, 0, 9, 3]
right_cloud = len(numbers)
temp = 0
i = 0

while i < right_cloud:
    if numbers[i] == 0:
        temp = numbers[right_cloud - 1]
        numbers[right_cloud - 1] = numbers[i]
        numbers[i] = temp
        right_cloud -= 1

    else:
        i += 1



print(numbers)