#Python Program to Count the Number of Digits and Letters in a String
s="kesava raju 8789"
letters=0
digits=0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i == " ":
        continue
    

print(letters)
print(digits)

