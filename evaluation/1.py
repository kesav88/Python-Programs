inp = input('enter the string: ')
res=" "
for i in inp:
    if i == " ":
        res += i 
    else:
        i = ord(i) + 1
        c = chr(i)
        res += c 
L = res.split()
print(L)
print(res)