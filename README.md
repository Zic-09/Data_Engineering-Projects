# 🔄 ETL Pipeline Projects with Python, MySQL, SQLite & Pandas

This repository showcases two simple but powerful **ETL (Extract, Transform, Load)** pipeline projects using Python, MySQL, SQLite, and Pandas. These projects demonstrate how real-world data is extracted from various sources, cleaned/transformed, and loaded into databases or data warehouses for reporting or analysis.

---

## 🧪 Project 1: MySQL to SQLite Data Warehouse Pipeline

### 🎯 Objective
Extract customer data from a MySQL database, transform the data (standardize country names), and load it into a **SQLite mini data warehouse** for further querying and reporting.

### 📦 Steps Performed

- **Extract**: Connect to MySQL and retrieve all rows from the `customers` table.
- **Transform**: Convert all country names to uppercase for consistency.
- **Load**: Load the transformed data into a new SQLite database (`data_warehouse.db`) into a table called `customer_warehouse`.
- **Query**: Perform a sample query on the SQLite warehouse to validate the pipeline.

### 💡 Real-Life Use Case
This mimics a **data migration or warehousing task**, such as:
- Moving data from production databases into analytics storage
- Creating dashboards or reports using lighter-weight systems
- Standardizing international customer data for marketing teams

---

## 🧪 Project 2: CSV to MySQL Data Pipeline

### 🎯 Objective
Read raw customer data from a CSV file, clean the data, and load it into a MySQL database.

### 📦 Steps Performed

- **Extract**: Load customer data from a local CSV file.
- **Transform**: Convert country names to *title case* (e.g., "nigeria" → "Nigeria") to ensure uniformity.
- **Load**: Insert the cleaned records into a MySQL table (`customers2`), creating the table if it doesn’t exist.

### 💡 Real-Life Use Case
This simulates what analysts or engineers do daily:
- Cleaning and importing data from spreadsheets
- Ingesting customer or survey data into structured databases
- Automating data ingestion for CRM systems or reporting

---

## 📊 Technologies Used

- **Python 3**
- **MySQL**
- **SQLite**
- **Pandas**
- **MySQL Connector**
- **CSV Files**

---

## 🧠 Key Concepts Demonstrated

- End-to-end ETL pipeline with Python
- Working with multiple databases (MySQL, SQLite)
- Data standardization using Pandas
- Automating data ingestion into SQL systems
- Connecting Python to real-world data storage

---

## 🚀 How to Run

### Prerequisites:
- Python installed
- MySQL Server installed and running
- MySQL user and schema created (e.g., `my_work_flow`)
- Required Python libraries:
```bash
pip install pandas mysql-connector-python

```
- Configure your database credentials in the scripts
- Run each script (etlpipeline1.py, etlpipeline2.py) from your terminal or IDE
- Observe the data loading, transformation, and results

### 👨‍💻 Author
Toluwanimi Oke
Data Analytics Engineer
🔗 [LinkedIn](www.linkedin.com/in/toluwanimi-oke-16763b228)  
🔗 [GitHub](https://github.com/Zic-09)
