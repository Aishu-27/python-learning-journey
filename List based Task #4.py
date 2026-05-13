nums=[]
for i in range(5):
    n=int(input("Enter 5 numbers:"))
    nums.append(n)
largest=nums[0]
for i in nums:
    if i > largest:
        largest = i
print(largest,"It is the largest number")
        
