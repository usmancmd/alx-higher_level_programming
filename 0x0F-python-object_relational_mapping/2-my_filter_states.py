#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(user=sys.argv[1],
                              password=sys.argv[2],
                              database=sys.argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM `states`\
                WHERE BINARY `name` = '{}'"
                .format(sys.argv[4]))
    for state in cur.fetchall():
        print(state)
