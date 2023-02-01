n=list(input("enter input elements: ").split(" "))
s={}
for i in n:
    c = n.count(i)
    if i not in s:
        i=str(i)
        s[i] = c


for i,v in s.items():
    print(f"{i} count is {v}")