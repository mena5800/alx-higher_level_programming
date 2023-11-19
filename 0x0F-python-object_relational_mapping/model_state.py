#!/usr/bin/python3

"""
this moudle to use orm (sqlalchemy).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a State entity in the database.

    Attributes:
    - id: An auto-generated, unique integer representing the primary key.
    - name: A string with a maximum length of 128 characters,
      representing the name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
