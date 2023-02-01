stones=input("enter a strings of stones: ")
jewels=input("enter a string of jewels: ")
count=0
for i in stones:
    if i in jewels:
        count += 1
print(count)