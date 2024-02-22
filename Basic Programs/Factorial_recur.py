
def fact_num(n):
    if n == 1:
             return n

    else:
        print("----")
        return n*fact_num(n-1)



num = 5
print(fact_num(5))