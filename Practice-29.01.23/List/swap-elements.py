#Python Program to Swap the First and Last Element in a List

l=[1,2,3,4,5,6,7,8]
leng=len(l)
l[0],l[leng-1] = l[leng-1],l[0]
print(l)