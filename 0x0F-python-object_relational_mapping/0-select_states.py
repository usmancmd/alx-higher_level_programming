#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
it take 3 arguments: mysql username, mysql password and database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
	connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

	cur = connection.cursor()
	cur.execute("SELECT * FROM `states` ORDER BY `states.id` ASC")

	query_rows = cur.fetchall()
	for state in query_rows:
		print(state)

	cur.close()
	connection.close()
