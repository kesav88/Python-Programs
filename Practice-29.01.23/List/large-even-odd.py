#Python Program to Print Largest Even and Largest Odd Number in a List

L=[100,2,19,8,7,6,5,4]
l_even=[]
l_odd=[]
for i in L:
    if i % 2 == 0:
        l_even.append(i)
    else:
        l_odd.append(i)
l_even.sort()
l_odd.sort()
l1=len(l_even)
l2=len(l_odd)
print(l_even[l1-1])
print(l_odd[l2-1])