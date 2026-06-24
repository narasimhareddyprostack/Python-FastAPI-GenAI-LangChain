#Extract data from Rest API
import requests
users=requests.get('https://jsonplaceholder.typicode.com/users').json()
print(users)
#Transform - for json file and csv file

#Load data into new json file and csv file