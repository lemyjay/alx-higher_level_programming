#!/usr/bin/python3
'''
A script that lists all cities from the database hbtn_0e_4_usa
'''


import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
        SELECT cities.id, cities.name, states.name\
        FROM cities, states\
        WHERE states.id = cities.state_id\
        ORDER BY id ASC'
    cursor.execute(query)
    cities = cursor.fetchall()

    # Display results
    for row in cities:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
