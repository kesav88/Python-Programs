#Python Program to Find the Sum of All the Items in a Dictionary
d={'a':1,'b':2,'c':3}
sum=0
v=list(d.values())
for i in v:
    sum += i
print(sum)
