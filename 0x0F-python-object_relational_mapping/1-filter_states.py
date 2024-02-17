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

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset='utf8'
        )
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
        sys.exit(1)

    # Execute SQL query to select all states
    try:
        cursor.execute('SELECT * FROM states WHERE name LIKE %s;', ('N%',))
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
