#Extract Data
import requests,csv,json,mysql.connector,pymongo

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

#Load in to 1)CSV File 2)JSON File

fp1=open('products.csv','w',newline='')
csv_writer=csv.writer(fp1)
#write csv file header
csv_writer.writerow(['pid','pname','price','category','rating'])
#write data into csv file 
csv_writer.writerows(beauty_products_csv_mysql)

print("New CSV File created successfully")