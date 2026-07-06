class Account:
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name 
        self.acc_bal=amount

a1=Account(101,'Rahul',5000)
a2=Account(102,'Sonia',6000)
a3=Account(103,'Priya',7000)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(Account.__dict__)