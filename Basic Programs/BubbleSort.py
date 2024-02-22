# Sorting a list using Bubble Sort technique

nums = [10, 4, 12, 67, 45, 1, 89, 32, 34]
k = len(nums) - 1
temp = 0

while k > 0:
  print(nums)
  i = 0
  j = i + 1
  while j <= k:
     if nums[i] > nums[j]:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

     i += 1
     j += 1


  k -= 1



print(nums)
