#Python Program to Count Number of Vowels in a String using Sets
str1="kesava"
s=set(str1)
#print(s)
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count += 1
print(count)