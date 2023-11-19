#!/usr/bin/python3

"""
this moudle to get access to database and print it.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""select cities.name from cities
              WHERE cities.state_id =
              (select id from states where states.name = %s)
              order by cities.id;
              """, (argv[4],))

    rows = cur.fetchall()

    result = ""
    for row in rows:
        result += row[0]
        result += ", "

    print(result[:-2])
    cur.close()
    db.close()
