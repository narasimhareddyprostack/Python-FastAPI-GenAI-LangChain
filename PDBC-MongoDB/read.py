from pymongo import MongoClient

try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['dbtwo']
    user_col=db['users']
    users=user_col.find()

    for user in users:
        print(user)

except Exception as err:
    print(err)