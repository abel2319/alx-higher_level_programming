#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name\
                FROM \
                `states` INNER JOIN `cities` \
                WHERE states.name='{}'".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
