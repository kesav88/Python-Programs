n=int(input("enter no of rows: "))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()