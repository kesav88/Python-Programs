n=input("enter a string")
l= int(len(n))
for i in n:
    if n[i] != n[l-i-1]:
        print("given string is not palindrome")
    else:
        print("given string is  palindrome")
