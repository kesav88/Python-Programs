def armstrong(num):
    if num<10:
        print(f'given number {num} is armstrong number')
    else:
        order=len(str(num))
        sum=0
        temp=num
        while num>0:
            last= num%10
            sum += last ** order
            num = num//10


        if sum==temp:
            print(f'given number {temp} is armstrong number')
        else:
            print(f'given number {temp} is not armstrong number')


armstrong(153)
