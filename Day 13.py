#Find Duplicate Element
nums=[1,2,2,3,2,5]
freq={}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for k in freq:
    if freq[k] > 1:
        print(k)
        
# Find largest Number in array
num=[8,3,15,2,10]
large=num[0]
for i in num:
    if i > large:
        large = i
print("The Largest number in array is:",large)

# Find Second Largest Number in Array
num=[8,3,15,2,10]
large1=num[0]
large2=num[1]
for i in num:
    if i > large1:
        large1 = i
for j in num:
    if j > large2 and j != large1:
        large2 = j
print("The Second Largest number in array is:",large2)
