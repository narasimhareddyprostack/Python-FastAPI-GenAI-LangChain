class GP:
    def m1(self):
        print("Grand Parent m1 method") 

class Parent(GP):
    def m2(self):
        print("Parent class  m2 method")  

class Child(Parent):
    def m3(self):
        print("Child class m3 method")  
c1=Child()
c1.m1()
c1.m2()
c1.m3()