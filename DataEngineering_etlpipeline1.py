import mysql.connector
import pandas as pd
import sqlite3

try:
# Connect to MySQL (Source)
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "************",
        database = "my_work_flow",
        port = 3306
    )
    if connection.is_connected:
        print("Connected to MySQL")
    else:
        print("Failed to Connect")
# Extracting Data
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers;")
        results = cursor.fetchall()
        for row in results:
            print(row)
except mysql.connector.Error as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
        print("MySQL Connection Closed")

# Convert to DataFrame
columns = ["id", "name", "email", "country", "created_at"]
df = pd.DataFrame(results, columns=columns)
print("Extracted Data:\n", df)

# Transforming Data
df["country"] = df["country"].str.upper() # standardize country names
print("\nTransformed Data:\n", df)

# Loading into SQLite (Mini Data Ware House)
sqlite_connection = sqlite3.connect("data_warehouse.db")
df.to_sql("customer_warehouse", sqlite_connection, if_exists="replace", index=False)
print("\nData Successfully Loaded into Data Warehouse!")

# Querying the Data Warehouse
ware_house = pd.read_sql("SELECT * FROM customer_warehouse", sqlite_connection)
print("\nWarehouse Data:\n", ware_house)