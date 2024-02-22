
def fib_recur(n):
    if n <= 1:
        return n

    else:
        return (fib_recur(n-1) + fib_recur(n-2))



for i in range (10):
    print(fib_recur(i))