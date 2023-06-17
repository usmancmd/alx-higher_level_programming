#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(user=sys.argv[1],
                              password=sys.argv[2],
                              database=sys.argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT `c`.`name`\
                 FROM `cities` as `c`\
                 JOIN `states` as `s`\
                 ON `c`.`state_id` = `s`.`id`\
                 WHERE `s`.`name`=%s", (sys.argv[4], ))

    new = []
    for city in cur.fetchall():
        new.append(city[0])
    print(', '.join(new))
