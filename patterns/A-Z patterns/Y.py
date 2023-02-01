for row in range(5):
    for col in range(5):
        if (row-col==0 and row<3) or ((row+col==4) and row<2) or (col==2 and row>2):
            print("*",end="")
        else:
            print(end=" ")
    print()