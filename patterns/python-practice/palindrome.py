n=int(input("enter a string: "))
temp=n
rev=0
while(n>0) :
    last=n%10
    rev=rev*10 + last
    n = n//10

if temp==rev:
    print(f"given number {temp} is a palindrome")
else:
        print(f"given number {temp} is not a palindrome")
