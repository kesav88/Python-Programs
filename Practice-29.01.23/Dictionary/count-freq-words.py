#Python Program to Count the Frequency of Each Word in a String using Dictionary
s="kesava raju raju kesava"
l=s.split()
count=0
d={}
for i in l:
    d[i]= l.count(i)

print(d)