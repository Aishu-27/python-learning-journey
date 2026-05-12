def largest_num(m,n):
    if m > n:
        return m
    else:
        return n
m,n =map(int,input("Enter 2 numbers:").split())
print(largest_num(m,n))


# Factorial using Function #

def factorial(n):
    fact = 1
    while n > 0:
        fact = fact*n
        n=n-1
    return fact
n=int(input("Enter a number:"))
print(factorial(n))

