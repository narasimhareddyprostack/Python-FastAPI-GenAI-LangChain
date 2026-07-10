#Extract Data
import requests
prod_resp=requests.get('https://dummyjson.com/products')
prod_data=prod_resp.json()
products=prod_data['products']
print(len(products))