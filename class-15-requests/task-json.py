#Extract data from Rest API
import requests,json
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
print(len(users))  #10
#Transform data- for json file and csv file
users_json=[]
for user in users:
    users_json.append({
        'uid':user['id'],
        'uname':user['username'],
        'city':user['address']['city'],
        'company':user['company']['name']
    })
print(len(users_json))
print(users_json)
#Load data into new json file and csv file
fp1=open('user.json','w')
json.dump(users_json,fp1)
print("New Data file created")