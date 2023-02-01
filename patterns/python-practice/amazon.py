class Amazon:
    def __init__(self):
        pass

    def select(self):
        chr = input("if you already existing customer please login else create account(l/n): ")
        if chr == "l":
            self.login()
        elif chr == "n":
            self.register()
    def login(self):
        user = input("enter your user name: ")
        passw = input("enter your password: ")
        if self.username == user and self.password == passw:
            print(f"{self.username} login is successful")
            self.items()
        else:
            print("enter your correct")

    def register(self,username,password,gmail,mobile):
        self.username = username
        self.password = password
        self.gmail = gmail
        self.mobile_no = mobile

    def items(self):
        item = ["tea","coffe","ginger","ilachi","greantea","lemontea"]
        ch = input("enter what do you want in capteria: ")
        if ch in item:
            print("your order is: ",ch)
            num = int(input("how many you want:"))
            print(f"{self.username} want to {num} {ch}s")
            cost = int(input("enter your item cost: "))
            print(f"{self.username} your total bill is: ", num * cost )


cust = Amazon()
cust.register("kesav","1234d","modi@gmail.com",8186942604)
cust.select()


