class Account: 
    min_bal=500 #static variable
    # class contains variable and methods
    
    def open_acc(self):
        print("Account Opened succesfully")

    def deposit(self):
        print("Amount Deposited succesfully")

    def withdrawl(self):
        print("Insuffient Bal")

    def get_bal(self):
        print("Server Always busy")
        
    def close_acc(self):
        print("your bal is -ve,pls deposit more")

a1=Account()
a1.open_acc()
a1.deposit()
a1.withdrawl()
a1.get_bal()
a1.close_acc()
