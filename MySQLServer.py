import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Update with your MySQL server host
            user='root',  # Update with your MySQL username
            password='obi1'  # Update with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            
    
    except mysql.connector.Error:
        print(f"Error while connecting to MySQL")

    finally:
        # Closing the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
