#Python Program to Find Largest Number in a List

L=[20,35,4,100,9]
lar=L[0]
for i in L:
    if i > lar:
        lar=i
print(lar)

# second method

# L.sort()
# leng=len(L)
# print(L[leng-1])