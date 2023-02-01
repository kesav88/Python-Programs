#Python Program to Find the Number Occurring Odd Number of Times in a List

L=[3,1,3,9,2,4,5,2,3,4,7,4,1,9]
l=[]
s=set(L)
for i in s:
    if L.count(i) % 2 == 0:
        continue
    else:
        l.append(i)
print(l)
