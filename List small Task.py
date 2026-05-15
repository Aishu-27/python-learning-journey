#Task 1
nums=[60,70,80,90,100]
print(nums[0:3])
print(nums[3:])
print(nums[::-1])

#Task 2
sats=[27,21,5]
sats.append(3)
print(sats)
sats.insert(5,89)
print(sats)
sats.remove(3)
print(sats)
sats.pop(2)
print(sats)

#Task 3
nums=[5,2,8,1,9]
nums.sort()
print(nums)
nums.reverse()
print(nums)

#Small Challenge
gums=[12,45,7,23,89,1]
print(gums[0:4])
print(gums[3:])
print(gums[::2])
print(gums[::-1])
print(gums.sort())
gums.sort(reverse=True)
print(gums)
gums.sort(reverse=False)
print(gums)
