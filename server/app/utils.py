import mysql.connector
from app.config import Config

def execute_query(query, params=None):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MySQLPassword@2004',
            database='crime'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
