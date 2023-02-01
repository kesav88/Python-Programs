n=int(input("enter no of terms: "))
n1=0
n2=1
sum=0
if n<0:
    print("enter number greater than zero")
else:
    for i in range(n):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2
