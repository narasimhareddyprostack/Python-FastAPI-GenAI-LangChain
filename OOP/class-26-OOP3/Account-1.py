class Account:
    branc="SBI Marathahalli"
    min_bal=5000 

    def __init__(self,id,name,amount):
        self.acc_id=id 
        self.acc_name=name 
        self.acc_bal=amount

    def deposit(self):
        pass 

    def withdrawl(self):
        pass 

    def get_bal(self):
        pass 

    def update_minbal(cls):
        pass 
    def cal_interest():
        roi=24
        return roi 
    


a1=Account(101,'RG',5000)
a2=Account(102,'SG',25000)

#print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)