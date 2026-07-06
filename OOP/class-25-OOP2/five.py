class Account:
    def __init__(self,id,name):
        print("Constructor Method")
        self.acc_id=id 
        self.acc_name=name

a1=Account(101,"RG")
a2=Account(102,"SG")
a3=Account(103,"PG")

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)