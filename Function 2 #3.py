def even_or_odd(i):
    if i % 2 == 0:
        return "Even"
    else:
        return "Odd"
i=int(input("Enter a number:"))
print(even_or_odd(i))

def pos_neg_0(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
n=int(input("Enter a number:"))
print(pos_neg_0(n))
