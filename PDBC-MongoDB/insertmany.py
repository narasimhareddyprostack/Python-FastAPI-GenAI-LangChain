from pymongo import MongoClient

try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['dbtwo']
    user_col=db['users']
    users=[{'uid':102,'uname':'Sonia'},{'uid':103,'uname':'Priya'}]
    user_col.insert_many(users)
    print("Document's inserted successfully")

except Exception as err:
    print(err)