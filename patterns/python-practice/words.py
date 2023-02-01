string='KESAVA'
print_K=[[" " for i in range(6)] for j in range(6)]
print_E=[[" " for i in range(7)] for j in range(5)]
print_S=[[" " for i in range(7)] for j in range(5)]
print_A=[[" " for i in range(6)] for j in range(5)]

#code for 'K'
for row in range(6):
    for col in range(6):
        if col==0 or (row+col==4) or (row-col==2):
            print_K[row][col]="*"

#code for 'E'
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3 or row==6) and col>0):
            print_E[row][col]="*"

# code for 'S'
for row in range(7):
    for col in range(5):
        if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==4 and (row==4 or row==5)) or (col==0 and (row==1 or row==2)):
           print_S[row][col]="*"

# code for 'A'
for row in range(6):
    for col in range(5):
        if ((col==0 or col==4)) or ((row==0 or row==3) and (col>0 and col<4)):
            print_A[row][col]="*"


for i in range(7):
    for j in range(5):
        print(print_K[i][j],end=" ")
    for j in range(5):
        print(print_E[i][j],end=" ")
    for j in range(5):
        print(print_S[i][j],end=" ")
    for j in range(5):
        print(print_A[i][j],end=" ")
    print()