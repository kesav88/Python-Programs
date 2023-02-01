#Python Program to Remove Duplicates from a List

L=[2,4,1,2,3,1,3,5,4,1]
# s=set(L)
# l=list(s)
# print(l)
l=[]
for i in L:
    if i in l:
        continue
    else:
        l.append(i)
print(l)
