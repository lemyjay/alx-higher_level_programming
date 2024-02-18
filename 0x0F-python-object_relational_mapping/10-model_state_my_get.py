#!/usr/bin/python3
'''
A script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database, pool_pre_ping=True)
            )

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects and print them
    state = session.query(State).filter(State.name == state_name).first()

    if (state):
        print(state.id)
    else:
        print("Not found")

    session.close()
