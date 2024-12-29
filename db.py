import mysql.connector as connector

try:
    database = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
    )

    cursor_obj = database.cursor()

    cursor_obj.execute('create database CRM')

    print("executed")
except:
    print("error")
finally:
    print("reached end")
