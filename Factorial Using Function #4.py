def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact * i
    return fact
num=int(input("Enter a number:"))
print(factorial(num))


#Check Prime
def checkPrime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2,num):
        if num % i == 0:
            return "Not Prime"

    return "Prime"
num=int(input("Enter a number:"))
print(checkPrime(num))
