#Python Program to Find the Length of a List using Recursion
def leng(L):
    if not L:
        return 0
    else:
        return 1 + leng(L[1:])


L=[1,2,3]
print("the length of given list is :",leng(L))