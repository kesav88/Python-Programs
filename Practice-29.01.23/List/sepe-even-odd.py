#Python Program to Split Even and Odd Elements into Two Lists
L=[1,2,3,4,5,6,7,8,9]
l_even=[]
l_odd=[]
for i in L:
    if i % 2 == 0:
        l_even.append(i)
    else:
        l_odd.append(i)
print(l_even)
print(l_odd)