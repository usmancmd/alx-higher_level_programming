#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(user=sys.argv[1],
                              password=sys.argv[2],
                              database=sys.argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name`\
                 FROM `cities` as `c`\
                 INNER JOIN `states` as `s`\
                 ON `c`.`state_id` = `s`.`id`\
                 ORDER BY `c`.`id`")
    for city_and_state in cur.fetchall():
        print(city_and_state)
