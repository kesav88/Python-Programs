n=int(input("enter the number: "))
a = 0
b = 1
c = 1
if (n==0 or n==1):
    ("given number is a fibonacci number")
else:
    while a < n:
        a = b+c
        c = b 
        b = a 
    if a == n:
        print(f"given number {n} is a fibonacci number")
    else:
        print(f"given number {n} is not a fibonacci number")