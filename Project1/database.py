import mysql.connector
import os
# Connecting to the database
def connection():
    return  mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="Hospital_management"
    )

