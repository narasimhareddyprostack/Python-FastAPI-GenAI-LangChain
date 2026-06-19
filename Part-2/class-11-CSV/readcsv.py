'''Write a python script to read csv file
   and print all employee names
'''
import csv
fp=open('emp.csv','r')
emp_csv_reader=csv.reader(fp)
employees=list(emp_csv_reader)

for emp in employees[1:]:
    print(emp[1])