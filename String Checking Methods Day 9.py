# isalpha
text="Aishwarya"
print(text.isalpha())

# isdigit
num="2707"
print(num.isdigit())

#isalnum
test="Aishu27"
print(test.isalnum())

#Concatenation
a="Hello"
b="World"
c="Iam Aishwarya"
print(a +" "+ b+" "+ c)

name="Aishwarya"
for ch in name:
    print(ch,end=" ")

# reverse
text = "Aishwarya"
print(text[::-1])
print("\n")

# Checking Vowels
text="Python programming"
count=0
for ch in text:
    if ch in "aeiou":
        count += 1
print(count)

#Palindrome
text="malayalam"
if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")

#Task 1
text="Python"
print(text[0])
print(text[5])
print(text[::-1])

#Task 2
text="hello world"
print(text.upper())
print(text.title())

#Task 3
s="madam"
if s == s[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")



