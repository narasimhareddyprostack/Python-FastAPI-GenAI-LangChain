#Extract Data
import requests
prod_resp=requests.get('https://dummyjson.com/products')
prod_data=prod_resp.json()
products=prod_data['products']
print(len(products))

#Tranform according requirement
beauty_products_csv_mysql=[]
for product in products:
    if product['category']=="beauty":
        beauty_products_csv_mysql.append((
            product['id'],
            product['title'],
            product['price'],
            product['category'],
            product['rating']
            ))


print(len(beauty_products_csv_mysql))
print(beauty_products_csv_mysql)