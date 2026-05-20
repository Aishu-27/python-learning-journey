# Warmup Questions
#Problem 1 Reverse
text="Hello"
print(text[::-1])

#Problem 2 Palindrome Check
text="madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Problem 3 COunt Vowels and Consonants
text="Python is a programming Language"
vowels=0
consonants=0
for ch in text:
    if ch in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Vowels:",vowels)
print("Consonants:",consonants)

#First Non-Repeating Character
text="aabbcddee"
freq={}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character:",ch)
        break

# Find Duplicate Characters in a String
text="Aishwarya"
freq={}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for ch in freq:
    if freq[ch] > 1:
        print(ch)

# Anagram
a="hello"
b="World"
result=""
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
        freq2[ch] =1
if freq1 == freq2:
    print("Anagram")
else:
    print("Not Anagram")
    
        
# Maximum Occuring Character
text="python programming"
freq={}
for ch in text:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1
max_count = 0
max_char = ""
for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch
print(max_char)
    
# Remove Duplicates from a String
text="aishwarya"
result=""
for ch in text:
    if ch not in result:
        result += ch
print(result)


# Character Frequency Counter
text="mississippi"
freq={}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)




































        
