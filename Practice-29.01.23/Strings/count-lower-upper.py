#Python Program to Count Number of Uppercase and Lowercase Letters in a String

s="KEsava RAju"
upper_count=0
lower_count=0
for i in s:
    if i == " ":
        continue
    if i.upper() == i:
        upper_count += 1
    elif i.lower() == i:
        lower_count += 1
    else:
        continue

print("the no of lower case letters are",lower_count)
print("the no of upper case letters are ",upper_count)
