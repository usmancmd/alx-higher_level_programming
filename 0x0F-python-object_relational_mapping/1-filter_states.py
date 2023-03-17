#!/usr/bin/env python3
"""
lists all states with a name starting 
with N (upper N) from the database hbtn_0e_0_usa
it take 3 arguments: mysql username, mysql password and database name
"""

import sys
import MySQLdb

connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = connect.cursor()
cur.execute("SELECT * FROM `states`")

query_rows = cur.fetchall()
for state in query_rows:
	if state[1][0] == "N":
		print(state)

connect.close()
