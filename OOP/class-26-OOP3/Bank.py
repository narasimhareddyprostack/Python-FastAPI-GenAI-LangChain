class Bank:
    min_bal=500   #static variable

    def open_account(self):
        print("Account Opened")

    @classmethod
    def update_min_bal(cls,amount):
        cls.min_bal=amount 

b1=Bank()
print(Bank.min_bal)
Bank.update_min_bal(600)
print(Bank.min_bal)