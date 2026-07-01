#Extract data from csv file
import csv 
fp1=open('user.csv','r')
csv_reader_obj=csv.reader(fp1)
users=list(csv_reader_obj)
print(len(users))