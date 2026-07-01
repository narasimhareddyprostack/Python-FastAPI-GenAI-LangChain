fp=None

try:
    fp=open("user.txt",'r')

except FileNotFoundError as err:
    fp=open("emp.txt",'r')

data=fp.read()
print(data)