#Python Program to Count the Number of Words and Characters in a String

s="kesav varma"

# to count no of words

res=s.split()
print("the no.of words in given string are ",len(res))
count=0
for i in s:
    if i == " ":
        continue
    else:
        count += 1
print("the no.of chars in the given string are ",count)