#!/usr/bin/python3

"""
this moudle contain City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """
    Represents a City entity in the database.

    Attributes:
    - id: An auto-generated, unique integer representing the primary key.
    - name: A string with a maximum length of 128 characters,
    representing the name of the city.
    - state_id: An integer representing the foreign key to the states.id column
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")
