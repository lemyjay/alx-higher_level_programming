#!/usr/bin/python3
'''
A script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
'''


import sys
from model_state import Base, State
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
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    '''
    Or it could have been done like this:
    session.query(State).filter(State.name.like('%a%')).delete()

    Then afterwards apply the commit to it
    '''

    session.commit()
    session.close()
