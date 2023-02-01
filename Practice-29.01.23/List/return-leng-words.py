#Python Program to Return the Length of the Longest Word from the List of Words

L=["kesava",'varma','raju','kanumuri']
# print(len(L))
l=[]
for i in L:
    l.append(len(i))

l.sort()
print(l[len(l)-1])