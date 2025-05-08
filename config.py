import mysql.connector
from mysql.connector import Error, cursor

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'test'
}

# Sql connection function
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        # print(f"Error connecting to database: {e}")
        return f'{e}'
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if connection:
    #         connection.close()
