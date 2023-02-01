for row in range(4):
    for col in range(7):
        if (col==0 or col==6) or (row+col==3) or (row==1 and col==4) or (row==2 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()