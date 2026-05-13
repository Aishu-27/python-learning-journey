rows=[10,50,30,90,70]
max1=rows[0]
max2=rows[0]
for i in rows:
    if i > max1 :
        max1 = i
for j in rows:
    if j > max2 and j != max1:
        max2 = i
print("1st Largest:",max1)
print("2nd Largest:",max2)
