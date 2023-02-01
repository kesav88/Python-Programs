def A():
    for row in range(6):
        for col in range(5):
            if ((col==0 or col==4)) or ((row==0 or row==3) and (col>0 and col<4)):
                print("*",end="")
            else:
                print(end=" ")
        print()

def B():
    for row in range(7):
        for col in range(5):
            if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
                print("*",end="")
            else:
                print(end=" ")
        print()


def C():
    for row in range(6):
        for col in range(5):
            if (col==0 and (row!=0 and row!=5)) or ((row==0 or row==5) and col>0):
                print("*",end="")
            else:
                print(end=" ")
        print()


def D():
    for row in range(7):
        for col in range(6):
            if col==0 or ((col==5 and (row>0 and row<6))) or ((row==0 or row==6) and col<5):
                print("*",end="")
            else:
                print(end=" ")
        print()

def E():
    for row in range(7):
        for col in range(5):
            if col==0 or ((row==0 or row==3 or row==6) and col>0):
                print("*",end="")
            else:
                print(end=" ")
        print()


def  F():
    for row in range(7):
        for col in range(5):
            if col==0 or ((row==0 or row==3) and col>0):
                print("*",end="")
            else:
                print(end=" ")
        print()


def G():
    for row in range(7):
        for col in range(6):
            if col==0 or (col==4 and (row!=1 and row!=2)) or ((row==0 or row==6) and (col>0 and col<4)) or (row==3 and col==5) or (row==col==3):
                print("*",end="")
            else:
                print(end=" ")
        print()

def H():
    for row in range(7):
        for col in range(5):
            if (col==0 or col==4) or (row==3 and (col>0 and col<4)):
                print("*",end="")
            else:
                print(end=" ")
        print()


def I():
    for row in range(7):
        for col in range(5):
            if (row==0 or row==6) or (col==2 and (row!=0 and row!=6)):
                print("*",end="")
            else:
                print(end=" ")
        print()


def J():
    for row in range(7):
        for col in range(5):
            if (row==0) or (row==6 and col<3) or (col==2 and (row!=0 and row!=6)):
                print("*",end="")
            else:
                print(end=" ")
        print()


def K():
    for row in range(7):
        for col in range(5):
            if col==0 or (row+col==4) or (row-col==2):
                print("* ",end="")
            else:
                print(end=" ")
        print()


def L():
    for row in range(7):
        for col in range(5):
            if col==0 or (row==6 and col>0):
                print("*",end="")
            else:
                print(end=" ")
        print()


def M():
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or (row-col==0 and row<4) or (row+col==6 and row<4):
                print("*",end="")
            else:
                print(end=" ")
        print()


def N():
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or ((row-col==0) and (col>0 and col<6)):
                print("*",end="")
            else:
                print(end=" ")
        print()

def O():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and (row>0 and row<6)) or ((row==0 or row==6) and (col>0 and col<4)):
                print("*",end="")
            else:
                print(end=" ")
        print()

def P():
    for row in range(7):
        for col in range(5):
            if col==0 or ((row==0 or row==3) and (col>0 and col<4)) or (col==4 and (row>0 and row<3)):
                print("*",end="")
            else:
                print(end=" ")
        print()

def Q():
    for row in range(8):
        for col in range(5):
            if (col==0 or col==4) and (row>0 and row<6) or (row==7 and col==3) or (row==5 and col==1) or ((row==0 or row==6) and (col>0 and col<4)):
                print("*",end="")
            else:
                print(end=" ")
        print()

def R():
    for row in range(7):
        for col in range(5):
            if col==0 or (col==4 and row!=0 and row!=3) or ((row==0 or row==3) and (col>0 and col<4)):
                print("*",end="")
            else:
                print(end=" ")
        print()

def S():
    for row in range(7):
        for col in range(5):
            if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==4 and (row==4 or row==5)) or (col==0 and (row==1 or row==2)):
                print("*",end="")
            else:
                print(end=" ")
        print()


def T():
    for row in range(7):
        for col in range(5):
            if row==0 or (col==2 and row!=0):
                print("*",end="")
            else:
                print(end=" ")
        print()


def U():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and row<6) or (row==6 and (col!=0 and col!=4)):
                print("*",end="")
            else:
                print(end=" ")
        print()


def V():
    for row in range(4):
        for col in range(7):
            if (row-col==0) or (row+col==6):
                print("*",end="")
            else:
                print(end=" ")
        print()


def W():
    for row in range(4):
        for col in range(7):
            if (col==0 or col==6) or (row+col==3) or (row==1 and col==4) or (row==2 and col==5):
                print("*",end="")
            else:
                print(end=" ")
        print()


def X():
    for row in range(5):
        for col in range(5):
            if (row+col==4) or (row-col==0):
                print("*",end="")
            else:
                print(end=" ")
        print()


def Y():
    for row in range(5):
        for col in range(5):
            if (row-col==0 and row<3) or ((row+col==4) and row<2) or (col==2 and row>2):
                print("*",end="")
            else:
                print(end=" ")
        print()

def Z():
    for row in range(6):
        for col in range(6):
            if (row==0 or row==5) or (row+col==5):
                print("*",end="")
            else:
                print(end=" ")
        print()


