import requests
import csv
import json
import mysql.connector
import pymongo


# ==========================
# Extract Data
# ==========================

def extract_products():
    """Fetch product data from API."""
    try:
        response = requests.get("https://dummyjson.com/products", timeout=10)
        response.raise_for_status()

        data = response.json()
        print(f"Total Products : {len(data['products'])}")

        return data["products"]

    except requests.exceptions.RequestException as err:
        print("Error while fetching API data:", err)
        return []


# ==========================
# Transform Data
# ==========================

def transform_products(products):
    """Filter beauty products and prepare data for CSV/MySQL and JSON/MongoDB."""

    csv_mysql_data = []
    json_mongo_data = []

    for product in products:

        if product.get("category") == "beauty":

            csv_mysql_data.append((
                product["id"],
                product["title"],
                product["price"],
                product["category"],
                product["rating"]
            ))

            json_mongo_data.append({
                "pid": product["id"],
                "pname": product["title"],
                "price": product["price"],
                "category": product["category"],
                "rating": product["rating"]
            })

    print(f"Beauty Products : {len(csv_mysql_data)}")

    return csv_mysql_data, json_mongo_data


# ==========================
# Load CSV
# ==========================

def write_csv(filename, data):
    """Write data into CSV file."""

    try:
        with open(filename, "w", newline="", encoding="utf-8") as fp:

            writer = csv.writer(fp)

            writer.writerow([
                "pid",
                "pname",
                "price",
                "category",
                "rating"
            ])

            writer.writerows(data)

        print(f"{filename} created successfully.")

    except Exception as err:
        print("CSV Write Error:", err)


# ==========================
# Load JSON
# ==========================

def write_json(filename, data):
    """Write data into JSON file."""

    try:
        with open(filename, "w", encoding="utf-8") as fp:
            json.dump(data, fp, indent=4)

        print(f"{filename} created successfully.")

    except Exception as err:
        print("JSON Write Error:", err)


# ==========================
# Load MySQL
# ==========================

def load_mysql(data):
    """Insert data into MySQL."""

    dbcon = None
    cursor = None

    try:
        dbcon = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dbtwo"
        )

        cursor = dbcon.cursor()

        sql = """
        INSERT INTO products
        (pid,pname,price,category,rating)
        VALUES(%s,%s,%s,%s,%s)
        """

        cursor.executemany(sql, data)

        dbcon.commit()

        print(f"{cursor.rowcount} records inserted into MySQL.")

    except mysql.connector.Error as err:
        print("MySQL Error:", err)

    finally:
        if cursor:
            cursor.close()

        if dbcon:
            dbcon.close()


# ==========================
# Load MongoDB
# ==========================

def load_mongodb(data):
    """Insert data into MongoDB."""

    client = None

    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        db = client["dbtwo"]

        collection = db["products"]

        collection.insert_many(data)

        print(f"{len(data)} records inserted into MongoDB.")

    except Exception as err:
        print("MongoDB Error:", err)

    finally:
        if client:
            client.close()


# ==========================
# Main Function
# ==========================

def main():

    products = extract_products()

    if not products:
        print("No data available.")
        return

    csv_data, json_data = transform_products(products)

    write_csv("products.csv", csv_data)

    write_json("products.json", json_data)

    load_mysql(csv_data)

    load_mongodb(json_data)


# ==========================
# Program Starts Here
# ==========================

if __name__ == "__main__":
    main()