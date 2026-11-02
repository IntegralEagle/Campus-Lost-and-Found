import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="campus_lost_found"
        )
        return connection
    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None
