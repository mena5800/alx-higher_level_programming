#!/usr/bin/python3

"""
this moudle to get access to database and print it.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    host_name = "localhost"
    port = 3306

    db_connection = MySQLdb.connect(
        host_name, username, password, database_name)

    cursor = db_connection.cursor()

    cursor.execute("""select *
    from states
    order by states.id """)

    m = cursor.fetchall()

    for row in m:
        print(row)

    cursor.close()
    db_connection.close()
