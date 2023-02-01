#Reverse the tuple
t=(1,2,3,4,5)
l=list(t)
s=0
end=len(t)-1
while (s < end):
    temp=l[s]
    l[s]=l[end]
    l[end]=temp
    s += 1
    end -=1

tup=tuple(l)
print(tup)