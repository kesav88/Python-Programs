n=[1,2,3,4,5]
l = len(n)-1
w=0
for i in range(l+1):
    w += n[l]
    l -= 1
print(w)