#How can you sort dictionary elements based on keys
d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
l=list(d.keys())
l.sort()
new_dic={}
for i in l:
    new_dic[i]= d[i]

print(new_dic)


