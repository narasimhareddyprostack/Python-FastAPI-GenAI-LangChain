class Test:
    a=100    #static or class variable


t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)