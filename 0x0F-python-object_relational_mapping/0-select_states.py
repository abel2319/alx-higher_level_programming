#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
The take 3 arguments: mysql username, mysql password and database
name (no argument validation needed)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER states.id ASCENDING")
    (print(state) for state in c.fetchall())
