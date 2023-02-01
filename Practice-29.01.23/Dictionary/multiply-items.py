#Python Program to Multiply All the Items in a Dictionary
d={'a':2,'b':2,'c':3}
v=list(d.values())
total=1
for i in v:
    total *= i

print(total)
