#!/usr/bin/env python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
## user = sys.argv[1]
## password = sys.argv[2]
## database name = sys.argv[3]

connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

## creating cursor
cur = connect.cursor()
cur.execute("SELECT * FROM `states`")

query_rows = cur.fetchall()
for state in query_rows:
	if state[1][0] == "N":
		print(state)

## closing the connection
cur.close()
connect.close()
