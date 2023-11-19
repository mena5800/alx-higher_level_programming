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

    cur.execute("""select * from states
              where name like "N%"
              order by states.id;
              """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
