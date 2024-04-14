#!/usr/bin/python3
"""
Change name of a State object
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object in the database
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_update = session.query(State).filter(State.id == '2').first()
    state_update.name = 'New Mexico'
    session.commit()

    # Closing the session
    session.close()
