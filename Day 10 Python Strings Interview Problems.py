# Character Frequency
text=input("Enter your input:")
freq={}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# Remove duplicates without set
text = "Aishwarya"
result=""
for ch in text:
    if ch not in result:
        result += ch
print(result)

# Using set
text='Aishwarya'
result=set(text)
print(result)

# Counting Words in Sentence
text="Aishwarya is coming from Coimbatore"
words=text.split()
print(len(words))

# Anagram without builtin function
a="silent"
b="listen"
freq1={}
freq2={}
for ch in a:
    if ch in freq1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1
for ch in b:
    if ch in freq2:
        freq2[ch] += 1
    else:
        freq2[ch] = 1
if freq1 == freq2:
    print("It is Anagram")
else:
    print("It is not Anagram")

# Anagram with builtin function
a="listen"
b="silent"
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")
    
# Toggle Case
text="Python Programming"
print(text.swapcase())

#Remove spaces
text = " Aishwarya Udhayakumar "
print(text.replace(" ",""))

# Largest Word in Sentence
text="Mesmapotomia is the Country it is also in this world"
words=text.split()
largest=max(words,key=len)
print(largest)

#Smallest Word in Sentence
text="Mesmapotomia is the Country it is also in this world"
words=text.split()
Smallest=min(words,key=len)
print(Smallest)

# Reverse each word in Sentence
text="Python is a Programming Language"
words=text.split()
for word in words:
    print(word[::-1], end=" ")
#Count Vowels and Consonants
text = "Agra is a Famous Place in India"
vowels=0
consonants=0
for ch in text:
    if ch in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("\n")
print("Vowels:",vowels)
print("Consonats:",consonants)

# Small Tasks 1
words="banana"
freq={}
for ch in words:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# Small Task 2
text="successful"
result=""
for ch in text:
    if ch not in result :
        result += ch
print(result)

# Small Task 3
a="heart"
b="earth"
freq1={}
freq2={}
for ch in a:
    if ch in freq1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1
for ch in b:
    if ch in freq2:
        freq2[ch] += 1
    else:
        freq2[ch] = 1
if freq1 == freq2:
    print("Anagram")
else:
    print("Not Anagram")

# Small Task 4
test="AI and Datascience"
word=test.split()
largest=max(word,key=len)
print(largest)

