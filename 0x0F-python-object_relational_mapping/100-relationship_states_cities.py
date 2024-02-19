#!/usr/bin/python3
'''
A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == '__main__':
    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database, pool_pre_ping=True)
            )

    # Creating the tables in the database
    Base.metadata.create_all(engine)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating the State "California" with the City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Adding the State and City objects to the session and committing changes
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Closing the session
    session.close()
