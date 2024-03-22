#!/usr/bin/python3
"""
python file that contains the class definition of a City.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Class City

    Attributes:
            __tablename__: table to reference
            id: id of object instance
            name: string of max 128 chars not null
            state_id: foreignKey
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
