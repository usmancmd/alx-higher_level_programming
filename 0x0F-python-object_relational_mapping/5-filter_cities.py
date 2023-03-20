#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
it take 3 arguments: mysql username, mysql password and database name
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """ not be executed when imported """
    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3])

    cur = connect.cursor()
    query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states ON cities.state_id=states.id \
            WHERE (states.name='{}')".format(sys.argv[4])

    cur.execute(query)
    state = cur.fetchall()
    length = len(state)

    for cities in state:
        for city in cities:
            length -= 1
            print(city, end="")
            if (length != 0):
                print(", ", end="")
            else:
                print()

    cur.close()
    connect.close()
