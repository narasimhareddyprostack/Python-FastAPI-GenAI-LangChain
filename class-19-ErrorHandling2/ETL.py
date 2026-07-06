import requests
import json
import csv

try:
    url = "https://dummyjson.com/products2334"
    response = requests.get(url)
    data = response.json()

    products_json = []
    products_csv = []

    for product in data["products"]:
        if product["category"] == "beauty":

            products_json.append({
                "Product_id": product["id"],
                "Name": product["title"],
                "Category": product["category"],
                "Price": product["price"],
                "Rating": product["rating"]
            })

            products_csv.append([
                product["id"],
                product["title"],
                product["category"],
                product["price"],
                product["rating"]
            ])

except requests.exceptions.RequestException as e:
    print("API Error:", e)

except Exception as e:
    print("Error:", e)

else:
    fp1 = open("product.json", "w")
    json.dump(products_json, fp1)

    fp2=open("product.csv", "w", newline="")
    csv_writer = csv.writer(fp2)
    csv_writer.writerow(["Product_id", "Name", "Category", "Price", "Rating"])
    csv_writer.writerows(products_csv)

    print("Files Created Successfully")

finally:
    print("Program Finished")