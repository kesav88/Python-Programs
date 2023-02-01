n=int(input())
i=0
for num in range(2, n+1):
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break

    if(i != num):
        print(num, end=" ")
