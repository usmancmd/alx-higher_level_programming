#!/usr/bin/python3
"""
script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
	""" to avoid executing the file when imported """
	connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

	cur = connection.cursor()
	cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (sys.argv[4],))
	query_rows = cur.fetchall()
	for state in query_rows:
		print(state)

	cur.close()
	connection.close()
