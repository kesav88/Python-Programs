#Python Program to Find Second Largest Number in a List

L=[1,20,3,40,50]
# leng=len(L)
# L.sort()
# print(L[leng-2])

# second way

larg=L[0]
sec_larg=L[0]
for num in L:
    if num > larg:
        sec_larg=larg
        larg=num
    elif num > sec_larg:
        sec_larg=num
print(sec_larg)