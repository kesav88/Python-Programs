#Python Program to Count Number of Lowercase Characters in a String

s="kesAva"
count=0
for i in s:
    if i.lower() == i:
        count += 1
print(count)