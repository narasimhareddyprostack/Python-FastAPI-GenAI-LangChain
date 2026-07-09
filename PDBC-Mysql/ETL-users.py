'''
invoke Rest API and write User data to users table
Usage: fetch all users
Rest API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Required Fiels:None 
Access Type:Public
'''

#Extract
import requests,mysql.connector
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
print(len(users))

#Transform
new_users=[]
for user in users:
    new_users.append((user['id'],
                      user['name'],
                      user['email'],
                      user['address']['city']
                      ))

#Load
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='dbtwo')
    cursor=dbcon.cursor()
    sql_st='''
            insert into users(user_id,uname,email,city)
            values(%s,%s,%s,%s);
            '''
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print("User Data inserted successfully")
except Exception as err:
    print(err)


