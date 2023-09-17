#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    host = "localhost"
    port = 3306
    db_connection = MySQLdb.Connect(
        host, username, password, db_name, port)
    cursor = db_connection.cursor()

    cursor.execute("""select cities.id, cities.name, states.name from states
                   right join cities
                   on cities.state_id = states.id
                   """)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db_connection.close()
