import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Creating a connection to MySQL Database server
        connection = mysql.connector.connect(
            host='localhost',  # Update with your MySQL server host
            user='root',  # Update with your MySQL username
            password=''  # Update with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        print(f"Could not connect to MySQL !!! Check connection details")

    finally:
        # Closing the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Done")

if __name__ == "__main__":
    create_database()
