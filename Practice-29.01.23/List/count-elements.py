#Python Program to Count Occurrences of Element in List
L=[3,2,9,4,3,1,2,4,5,4,9]
s=set(L)
# print(s)
for i in s:
    print(i,"is present",L.count(i),"times")
