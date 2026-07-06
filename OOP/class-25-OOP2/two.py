class Test:
    a=100    #static or class variable

    def m1(self):
        self.b=200  #instance var
        self.c=300  #instance var

    @classmethod
    def m2(cls):
        Test.d=400
        cls.e=500
t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)
print("After calling m1 method id instance method")
t1.m1()
t1.m2()
print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)