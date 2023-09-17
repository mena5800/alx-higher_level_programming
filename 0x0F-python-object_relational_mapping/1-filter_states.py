#!/usr/bin/python3
"""this module is use to fiter database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    host = "localhost"
    port = 3306

    db_connection = MySQLdb.Connect(host, username, password, db_name, port)
    cursor = db_connection.cursor()

    cursor.execute("""select * from states
                   where name like 'N%'
                   order by states.id;""")

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()
