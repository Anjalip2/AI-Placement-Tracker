from modules.database import get_connection

try:
    connection = get_connection()
    if connection.is_connected():
        print("connected to MySQL successfully!")
        connection.close()

except Exception as e:
    print("connection failed!")
    print(e)