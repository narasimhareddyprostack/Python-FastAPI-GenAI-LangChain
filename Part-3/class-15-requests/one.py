
'''
Usage: fetch Users
Rest API URL: https://jsonplaceholder.typicode.com/users
Method Type:GET
Req Fields: None
Access Type:Public
'''
import requests
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()
status_code=resp_data.status_code
#print(users)
print(status_code)

for user in users:
    print(user['username'])