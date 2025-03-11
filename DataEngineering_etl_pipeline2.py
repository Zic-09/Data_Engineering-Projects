import mysql.connector
import pandas as pd

# Extraction - Read CSV File
df = pd.read_csv("C:/Users/HP/Desktop/My Personal Data Projects/etlpipeline file.csv")
print(df.head())

# Transformation - Convert country column values to proper case
df["country"] = df["country"].str.title()
print("\nTransformed Data:\n", df)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Oluwadarasimi18",
    database="my_work_flow",
    port = 3306
)

cursor = connection.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers2 (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(20),
        country VARCHAR(100)
    )
""")

# Insert Data
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO customers2 (id, name, email, phone, country) VALUES (%s, %s, %s, %s, %s)",
        (row["id"], row["name"], row["email"], row["phone"], row["country"])
    )

connection.commit()
cursor.close()
connection.close()

print("✅ Data Loaded into MySQL Successfully!")


