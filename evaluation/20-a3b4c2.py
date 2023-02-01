str1 = "aaabbbcccdddda"
k = {}
for i in str1:
    if i in k.keys():
        k[i] += 1
    else:
        k[i] = 1

res = ""
for key,val in k.items():
    res += key+str(val)
print(res)