# Check if a number is Prime #
def prime(num):
    for i in range(2,num):
        return "Not Prime"
    return "Prime"
num=int(input("Enter a number:"))
print(prime(num))
        
        
