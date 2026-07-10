#Extract Data
import requests,csv,json,mysql.connector,pymongo

prod_resp=requests.get('https://dummyjson.com/products')
prod_data=prod_resp.json()
products=prod_data['products']
print(len(products))

#Tranform according requirement
beauty_products_csv_mysql=[]
beauty_products_json_mongodb=[]
for product in products:
    if product['category']=="beauty":
        beauty_products_csv_mysql.append((
            product['id'],
            product['title'],
            product['price'],
            product['category'],
            product['rating']
            ))
        beauty_products_json_mongodb.append({
            'pid':product['id'],
            'pname':product['title'],
            'price':product['price'],
            'category':product['category'],
            'rating':product['rating']
        })


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


try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='dbtwo')
    cursor=dbcon.cursor() 
    sql_st='''
            insert into products(pid,pname,price,category,rating)
            values(%s,%s,%s,%s,%s);
        '''
    cursor.executemany(sql_st,beauty_products_csv_mysql)
    dbcon.commit()
    print("Data inserted successfully")

except Exception as err:
    print(err) 
finally:
    cursor.close()
    dbcon.close() 

fp2=open('products.json','w')
json.dump(beauty_products_json_mongodb,fp2)
print("New JSON File Created Successfully")

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/') 
    db=client['dbtwo']
    product_col=db['products']
    product_col.insert_many(beauty_products_json_mongodb)
    print("Product Data inserted into collection successfully")

except Exception as err:
    print(err)