#How to get min and max keys corresponding to min and max value in Dictionary
fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
v=list(fruitsDict.values())
v.sort()
min=0
max=0
for k,val in fruitsDict.items():
    if v[len(v)-1] == val:
        max= k
    elif v[0] == val:
        min= k

print(min)
print(max)
