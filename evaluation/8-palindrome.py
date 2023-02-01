n=int(input("enter a number: "))
temp=n
res=0
while n>=0:
    last = temp%10
    res = res * 10 + last
    temp = temp//10
if n == res:
    print("its palindrome")
else:
    print("its not apalindrome")