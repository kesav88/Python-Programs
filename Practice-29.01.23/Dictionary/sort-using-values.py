#How can you sort the dictionary elements based on values
d = {'Tim': 18, 'Charlie': 120, 'Tiffany': 22, 'Robert': 25}
k=list(d.values())
k.sort()
new_dic={}
leng=len(k)-1
while leng >= 0:
    for i,v in d.items():
        if v == k[leng]:
            new_dic[i] = k[leng]
            leng -=1

print(new_dic)

