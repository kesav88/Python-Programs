#Python Program to Map Two Lists into a Dictionary
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
d={}
i=0
while i < len(l1):
    d[l1[i]] = l2[i]
    i +=1

print(d)