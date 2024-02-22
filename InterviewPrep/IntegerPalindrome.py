
num = 254
rev_num = 0

while num > 0:

   res = num % 10
   rev_num = rev_num * 10 + res
   num = num//10


print(rev_num)