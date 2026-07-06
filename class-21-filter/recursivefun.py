def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

print(fact(6))

'''
5*fact(4)
5*4*fact(3)
5*4*3*fact(2)
5*4*3*2*fact(1)
5*4*3*2*1
'''