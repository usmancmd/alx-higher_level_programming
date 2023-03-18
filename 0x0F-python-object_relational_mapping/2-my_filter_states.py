#!/usr/bin/python3
"""
script that takes in an argument 
and displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == "__main__":
	""" not be executed when imported """
	connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

	cur = connect.cursor()
	query = "SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(sys.argv[4])
	cur.execute(query)

	query_rows = cur.fetchall()
	for state in query_rows:
		print(state)

	connect.close()
