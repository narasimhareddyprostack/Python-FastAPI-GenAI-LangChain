import json 
import csv 

fp1=open('emp.json','r')
employees=json.load(fp1)
print(type(employees))
print(len(employees))

#Transfor
female_employees=[]
for emp in employees:
    female_employees.append([emp['eid'],
                             emp['ename'],
                             emp['gender']])
print(female_employees)