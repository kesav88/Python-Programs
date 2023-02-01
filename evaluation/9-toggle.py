n = "Hello World"
k = " "
for i in n:
    if i.upper()==i:
        i = i.lower()
        k += i
       
    else:
        i = i.upper()
        k += i
print(k)