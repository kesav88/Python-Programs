inp=input("enter a string:")
res=''
for i in inp:
    if inp.count(i)==1:
        res += i
print(res)