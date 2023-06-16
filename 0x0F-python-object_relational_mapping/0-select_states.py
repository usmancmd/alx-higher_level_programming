#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(user=sys.argv[1],
                              password=sys.argv[2],
                              database=sys.argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM `states`")
    for state in cur.fetchall():
        print(state)
