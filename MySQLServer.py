import mysql.connector
from mysql.connector import Error

def connect_to_database():
"""Connect to the alx_book_store database."""
try:
connection = mysql.connector.connect(
host='localhost',        # Update if using a remote host
user='root',             # Replace with your MySQL username
password='your_password',# Replace with your MySQL password
database='alx_book_store'
)

```
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record[0]}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
```

if **name** == "**main**":
connect_to_database()
