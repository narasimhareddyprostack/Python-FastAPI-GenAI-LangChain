#Extract data from Rest API
import requests,json,csv
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
print(len(users))  #10
#Transform data- for json file and csv file
users_json=[]
users_csv=[]
for user in users:
    users_json.append({
        'uid':user['id'],
        'uname':user['username'],
        'city':user['address']['city'],
        'company':user['company']['name']
    })
    users_csv.append([user['id'],
                      user['username'],
                      user['address']['city'],
                      user['company']['name']]
                      )
#print(len(users_json))
#print(users_json)
#Load data into new json file and csv file
fp1=open('user.json','w')
fp2=open('user.csv','w',newline="")
json.dump(users_json,fp1)
print("New Data file created")
csv_writer=csv.writer(fp2)
#write csv file header
csv_writer.writerow(["Id","User Name","City","Company Name"])
csv_writer.writerows(users_csv)
print("New JSO and CSV file created Successfully")