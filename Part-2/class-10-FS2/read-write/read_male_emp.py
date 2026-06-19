'''
Write a python script
a)read emp.json file and print all employee names
b)read emp.json file and print all male employee names
c)read emp.json file and print no of female employees
'''
import json 
fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))  #<class,list>

for emp in employees:
    if emp['gender']=="Male":
        print(emp['ename'],"-",emp['gender'])