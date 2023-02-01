n = "hello world"
k = ""
for i,v in enumerate(n):
    if i % 2 !=0:

        if v.upper()==v:
            v = v.lower()
            k += v
        
        else:
            v = v.upper()
            k += v
    else:
        k += v
    
print(k)