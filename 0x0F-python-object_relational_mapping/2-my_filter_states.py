#!/usr/bin/env python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
	""" not be executed when imported """
	connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

	cur = connect.cursor()
	query = "SELECT * FROM `states` WHERE '{}' LIKE BINARY '{}'".format(sys.argv[3], sys.argv[4])
	cur.execute(query)

	query_rows = cur.fetchall()
	for state in query_rows:
		print(state)

	connect.close()
