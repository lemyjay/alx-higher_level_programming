#!/usr/bin/python3
'''
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
'''


import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset='utf8'
    )
    cursor = db.cursor()

    # Execute SQL query to select all states
    query = 'SELECT * FROM states WHERE name = %s ORDER BY id ASC'
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    # Display results
    for state_id, state_name in states:
        print("({}, '{}')". format(state_id, state_name))

    # Close cursor and database connection
    cursor.close()
    db.close()
