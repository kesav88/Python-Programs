#Python Program to Count the Number of Vowels in a String

s="kesava"
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count += 1

print(count)