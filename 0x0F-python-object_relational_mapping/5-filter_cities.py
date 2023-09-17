#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    host = "localhost"
    port = 3306
    db_connection = MySQLdb.Connect(
        host, username, password, db_name, port)
    cursor = db_connection.cursor()

    cursor.execute("""select cities.name from states
                   right join cities
                   on cities.state_id = states.id
                   where states.name = "{}"
                   order by cities.id;
                   """.format(state_name))

    result = cursor.fetchall()
    output = ""
    for i in range(len(result)):
        output += result[i][0]
        if i != len(result) - 1:
            output += ", "
    print(output)

    cursor.close()
    db_connection.close()
