#!/usr/bin/env python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
## user = sys.argv[1]
## password = sys.argv[2]
## database name = sys.argv[3]
## state name searched = sys.argv[4]

if __name__ == "__main__":
	""" not be executed when imported """
	connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

	## creating cursor
	cur = connect.cursor()
	query = "SELECT * FROM `states` WHERE '{}' LIKE BINARY '{}'".format(sys.argv[3], sys.argv[4])
	cur.execute(query)

	query_rows = cur.fetchall()
	for state in query_rows:
		print(state)

	## closing the connection
	connect.close()
