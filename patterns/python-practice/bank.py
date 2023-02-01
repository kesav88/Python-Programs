class AxisBank:
    bank_na = "AXIS bank"
    branch = "chennai"
    pincode = 600094

class Customer(AxisBank):
    def __init__(self,firstname,lastname,accountno,balance):
        self.lname = firstname
        self.fname = lastname
        self.acno = accountno
        self.bal = balance

    def details(self):
        print(f"branch name:{self.branch}")
        print(f"pincode:{self.pincode}")
        print(f"lastname:{self.lname}")
        print(f"firstname:{self.fname}")
        print(f"account number:{self.acno}")
        print(f"your balanceis:{self.bal}")
    
    def select(self):
        select = input("if you enter w or d:")
        if select == "w":
           print(self.withdraw())
        elif select == "d":
            print(self.deposite())
        elif select == "ms":
            print(self.mini_statement())
    def mini_statement(self):
        print("****/**welcome to axis bank**/****")
        print(f"UserName: {self.fname} {self.lname}")
        print(f"Account Number: {self.acno}")
        print(f"your balance is: {self.bal}")
        print("****/** Thankyou for visiting our Axis bank ATM **/****")
    def deposite(self):
        amt = int(input("enter your deposite amount: "))
        self.bal += amt
        print(f"dear {self.bank_na} customer yor deposite is successful")
        print(f"{self.fname} your curent balance is:{self.bal}")
    
    def withdraw(self):
        amt = int(input("enter your withdraw amount: "))
        if self.bal >= amt:
            self.bal -= amt
            print(f"dear {self.bank_na} user your withdraw is successfull")
            print(f"{self.fname} your current balance is:{self.bal}")
        else:
            print("insuffient balance")
        return


kesav = Customer("raju","kesav",1555123,5000)
kesav.details()
kesav.select()