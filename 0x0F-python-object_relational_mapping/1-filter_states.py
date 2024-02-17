#!/usr/bin/python3
'''
A script that lists all states with a name starting with N (upper N)
from the database hhbtn_0e_0_usa
'''


import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset='utf8'
    )
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC;',
        ('N%',))
    states = cursor.fetchall()

    # Display results
    # Display results
    for state_id, state_name in states:
        if state_name[0] == 'N':
            print("({}, '{}')".format(state_id, state_name))

    # Close cursor and database connection
    cursor.close()
    db.close()
