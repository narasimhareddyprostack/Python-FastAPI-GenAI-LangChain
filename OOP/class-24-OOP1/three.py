class Account:
    """  Accoun class created by Narasimha in weekend """
    min_bal=500 #static variable

    def open_acc(self):
        print("Account Opened success")

a1=Account()
a2=Account()
print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)