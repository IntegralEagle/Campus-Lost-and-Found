from db_connection import get_connection

connection = get_connection()

if connection and connection.is_connected():
    print("Connected to campus_lost_found successfully!")

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")

    print("Available tables:")
    for table in cursor.fetchall():
        print(table[0])

    cursor.close()
    connection.close()
else:
    print("Connection failed. Check your settings.")
