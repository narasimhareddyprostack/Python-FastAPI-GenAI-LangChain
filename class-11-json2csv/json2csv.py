import json 
import csv 
#Extract Data from json file
fp1=open('emp.json','r')
employees=json.load(fp1)


#Transform for csv file
female_employees=[]
for emp in employees:
    if emp['gender']=="Female":
        female_employees.append([emp['eid'],
                             emp['ename'],
                             emp['gender']])
print(female_employees)

#Load
fp2=open('user.csv','w',newline="")
csv_writer=csv.writer(fp2)
csv_writer.writerow(['uid','uname','gende'])
csv_writer.writerows(female_employees)

print("New CSV File created succesfully")