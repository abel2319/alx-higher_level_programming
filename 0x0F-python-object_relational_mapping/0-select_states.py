#/usr/bin/python3
'''

'''
import sys
import MySQLdb

if __name__ == "__main__":
    db= _mysql.connect(host="localhost", port=3306,
                       user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER states.id ASCENDING")
    (print(state) for state in c.fetchall())

