#Array
arr=[10,20,30,40,50]
print(arr)

#Accessing Elements
print(arr[1])
print(arr[3])

#Negative Elements
print(arr[-5])
print(arr[-2])
print(arr[-1])

#Traversing an Array
for num in arr:
    print("Traverse array:",num)

#Updateing Element
arr=[10,20,30,40,50]
arr[3]=27
print(arr)

#Length of an Array
print("Length of Array:",len(arr))

#Maximum element in Array
print("Maximum Element in Array:",max(arr))
print("Minimum Element in Array:",min(arr))

max1=arr[0]
min1=arr[0]
for i in arr:
    if i > max1:
        max1 = i
    if i < min1:
        min1 = i
print(max1)
print(min1)

# Sum of Array Elements
print(sum(arr))

# Sum of Array without using builtin function
total = 0
for i in arr:
    total += i
print(total)




