#!/usr/bin/python3

"""script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa.
"""

import sqlalchemy
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name == sys.argv[4]).first()

    if states:
        print(states.id)
    else:
        print("Not found")
