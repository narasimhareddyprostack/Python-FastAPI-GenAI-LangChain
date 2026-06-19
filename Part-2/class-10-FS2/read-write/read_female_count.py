import json 

fp=open('emp.json','r')
employees=json.load(fp)
female_counter=0

for emp in employees:
    if emp['gender']=="Female":
        female_counter=female_counter+1

print("No  Femla Emplyees",female_counter)