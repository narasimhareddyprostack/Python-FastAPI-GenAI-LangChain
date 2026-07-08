class Parent1:
    def m1(self):
        print("Parent1 Class m1 method")

    def m2(self):
        print("Parent1 Class m2 method")  

class Parent2:
    def m2(self):
        print("Parent2 Class m2 method")

class Child(Parent2,Parent1):
    def m3(self):
        print("Child Class m3 metohd")
c1=Child()

c1.m1()
c1.m2()
c1.m3()