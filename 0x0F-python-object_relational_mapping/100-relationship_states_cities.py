#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
   from the database
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.schema import Table


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add_all([new, new_city])
    session.commit()
    session.close()
