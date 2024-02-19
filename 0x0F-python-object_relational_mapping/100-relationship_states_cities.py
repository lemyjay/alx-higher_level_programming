#!/usr/bin/python3
'''
A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database, pool_pre_ping=True)
            )

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State
    california = State(name="California")

    # Create a new City
    san_francisco = City(name="San Francisco")

    # Add the city to the state
    california.cities.append(san_francisco)

    # Add the state to the session
    session.add(california)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
