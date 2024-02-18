#!/usr/bin/python3
'''
A script that prints all City objects from the
database hbtn_0e_6_usa
'''


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    # Querying for the State instance with 'a' in their name
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
