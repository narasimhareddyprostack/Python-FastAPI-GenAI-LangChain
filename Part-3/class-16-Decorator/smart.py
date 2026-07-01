'''
Decorator is functoin, it takes function as argument
and modifiy the functionality and return
'''
def smart_div(func):
    def inner(a,b):
        if b==0:
            print("Can't Divide by Zero")
        else:
            return func(a,b)   
    return inner