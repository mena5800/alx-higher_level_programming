#!/usr/bin/python3

"""prints all City objects from the database hbtn_0e_14_usa
"""

import sqlalchemy
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    # Query cities and states, and display the results
    cities_and_states = session.query(
        City, State).join(State).order_by(City.id).all()

    # Display the results in the specified format
    for city, state in cities_and_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session to release resources
    session.close()
