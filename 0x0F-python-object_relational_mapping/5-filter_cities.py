#!/usr/bin/python3
'''
A script that taskes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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

    # Execute SQL query
    query = '\
        SELECT name\
        FROM cities\
        WHERE state_id = (\
            SELECT id\
            FROM states\
            WHERE name = %s\
        )\
        ORDER BY cities.id ASC'
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    # Display results
    for row in cities:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
