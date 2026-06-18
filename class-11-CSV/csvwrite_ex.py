import csv 
employees=[
    [1,'Rahul','Male'],
    [2,'Sonia','Female'],
    [3,'Priyanka','Female'],
    [4,'Modi','Male'],
    [5,'Amith','Male']
]

fp=open('user.csv','w',newline="")
csv_writer=csv.writer(fp)
#write csv header using writerow() method
csv_writer.writerow(["uid","uname","gender"])
csv_writer.writerows(employees)
print("New CSV File created successfully!")