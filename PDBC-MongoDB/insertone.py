from pymongo import MongoClient

try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['dbtwo']
    user_col=db['users']
    user_col.insert_one({'uid':101,'uname':'RG'})
    print("Document inserted successfullt")

except Exception as err:
    print(err)