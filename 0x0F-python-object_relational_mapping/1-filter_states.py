#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(user=sys.argv[1],
                              password=sys.argv[2],
                              database=sys.argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in cur.fetchall():
        if state[1][0] == "N":
            print(state)
