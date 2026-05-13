def sumOfNatural_nums(n):
    total=0
    for i in range(1,n+1):
        total += i
    return total
n=int(input("Enter a range of number:"))
print(sumOfNatural_nums(n))
