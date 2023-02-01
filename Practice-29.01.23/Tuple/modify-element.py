#Write a program to modify the first item (11) of a list inside a following tuple to 22
#tuple1 = (11, [11, 33], 44, 55)

tup1=(11, [11, 33], 44, 55)
tup1[1][0] = 22
print(tup1)