chiks=[1,12,24,56,78,89,90]
max_elem=chiks[0]
min_elem=chiks[0]
for i in chiks:
    if i > max_elem:
        max_elem = i
  
    elif i < min_elem:
        min_elem = i

print("Largest number is:",max_elem)
print("Smallest number is:",min_elem)
