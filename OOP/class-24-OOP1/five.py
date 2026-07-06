class Account:
    min_bal=500

    def open_account(self):
        self.name="Rahul"

a1=Account()
a1.open_account()
print(a1.__dict__)