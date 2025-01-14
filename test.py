import mysql.connector
from mysql.connector import Error


def connect():
    try:
        connect = mysql.connector.connect(
            host='185.92.74.31',
            user='Gonna_Destroy',
            password='zaqxsw123',
            database='wifi',
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            auth_plugin='mysql_native_password'
        )

        cursor = connect.cursor()

        cursor.execute('INSERT INTO users (ssid, passwd) VALUES (%s,%s) ', ('test', '1111'))
        connect.commit()

        cursor.close()
        connect.cursor()
    except Error as e:
        print(e)

