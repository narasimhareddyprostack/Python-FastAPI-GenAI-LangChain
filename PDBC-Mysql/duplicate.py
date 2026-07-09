import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL
    dbcon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="dbtwo"
    )

    cursor = dbcon.cursor()

    # Delete duplicate rows while keeping the smallest id
    delete_query = """
        DELETE u1
        FROM users u1
        INNER JOIN users u2
            ON u1.user_id = u2.user_id
           AND u1.user_id > u2.user_id;
    """

    cursor.execute(delete_query)
    dbcon.commit()

    print(f"{cursor.rowcount} duplicate records deleted successfully.")

except Error as e:
    print("Database Error:", e)

finally:
    if cursor:
        cursor.close()

    if dbcon.is_connected():
        dbcon.close()