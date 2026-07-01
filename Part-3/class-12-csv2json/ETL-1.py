#Extract data from csv file
import csv,json
fp1=open('user.csv','r')
csv_reader_obj=csv.reader(fp1)
users=list(csv_reader_obj)
print(len(users))
#transform
employee_data=[]
#how to exclude csv header? using list slicing
for user in users[1:]:
    employee_data.append({"eid":user[0],
                          "ename":user[1],
                          "gender":user[2]
                          })

#print(employee_data)
fp2=open('emp.json','w')
json.dump(employee_data,fp2)
print("New JSON File Created Successfully")