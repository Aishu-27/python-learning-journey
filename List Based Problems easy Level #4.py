#EASY
#Count Even or Odd Number
seats=[1,2,3,4,5]
odd=0
even=0
for i in seats:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:",even)
print("Odd:",odd)

# Find Sum of Even Numbers
n=[1,2,3,4,]
sum = 0
even=0
for i in n:
    if i % 2 == 0:
        sum = sum + i
print("Sum:",sum)

#Search Element in List
element=[10,20,30,40,50]
search = int(input("Enter element to be search:"))
for i in range(len(element)):
    if element[i] == search:
        print("Found at index:",i)
        break
    else:
        print("Element not Found")
