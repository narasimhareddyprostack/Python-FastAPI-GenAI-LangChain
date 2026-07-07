class Account:
    branc="SBI Marathahalli"
    min_bal=500 

    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_name=name 
        self.acc_bal=amount

    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount 

    def withdrawl(self,amount):
        self.acc_bal=self.acc_bal-amount  

    def get_bal(self):
        return self.acc_bal-Account.min_bal 
    @classmethod
    def update_minbal(cls):
        cls.min_bal=600

    @staticmethod
    def cal_interest():
        roi=24
        return roi 
    


a1=Account(101,'RG',5000)
a2=Account(102,'SG',25000)

#print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)

a1.deposit(500)
print("*****************")

print(a1.acc_bal)
print(a2.acc_bal)

print("Withdrawl")
a2.withdrawl(5500)
print(a2.acc_bal)
print("***************** ")
print(a1.get_bal())
print(a2.get_bal())

print('Access- class method to update min bal')

Account.update_minbal()

print("***************** ")
print(a1.get_bal())
print(a2.get_bal())
