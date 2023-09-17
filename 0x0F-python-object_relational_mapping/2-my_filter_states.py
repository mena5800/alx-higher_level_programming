#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of 
hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    search_term = argv[4]
    host = "localhost"
    port = 3306

    db_connection = MySQLdb.Connect(host, username, password, db_name, port)
    cursor = db_connection.cursor()

    cursor.execute("""select * from states
                   where states.name = '{}'
                   order by states.id;""".format(search_term))

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()
